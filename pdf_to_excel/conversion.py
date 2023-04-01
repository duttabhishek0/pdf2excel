import tabula

def convert_pdf_to_excel(pdf_path, output_path):
    # Read PDF and extract tables
    tables = tabula.read_pdf(pdf_path, pages='all')
    
    # Save tables as CSV files
    for i, table in enumerate(tables):
        csv_path = output_path.replace('.xlsx', f'_{i}.csv')
        table.to_csv(csv_path, index=False)
    
    # Merge CSV files into Excel file
    xlsx_path = output_path
    if len(tables) > 1:
        xlsx_path = xlsx_path.replace('.xlsx', '_merged.xlsx')
        tabula.convert_into([csv_path for csv_path in output_path.glob('*.csv')],
                            xlsx_path, output_format='xlsx', pages='all')
    elif len(tables) == 1:
        tables[0].to_excel(xlsx_path, index=False)
    else:
        raise ValueError('No tables found in PDF')
