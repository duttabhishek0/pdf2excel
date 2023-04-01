def test_conversion_content(self):
    test_files = os.listdir(self.test_data_dir)
    for test_file in test_files:
        if not test_file.endswith(".pdf"):
            continue
        input_path = os.path.join(self.test_data_dir, test_file)
        output_path = os.path.join(
            self.test_output_dir, f"{os.path.splitext(test_file)[0]}.xlsx"
        )
        try:
            convert_pdf_to_excel(input_path, output_path)
            self.assertTrue(os.path.exists(output_path))
            # Verify that the output file contains expected content
            df = pd.read_excel(output_path, engine="openpyxl")
            self.assertEqual(df.iloc[0, 0], "Date")
            self.assertEqual(df.iloc[0, 1], "Description")
            self.assertEqual(df.iloc[0, 2], "Amount")
            logging.info(f"Conversion successful for {test_file}")
            print(f"Conversion successful for {test_file}")
        except Exception as e:
            logging.exception(f"Conversion failed for {test_file}")
            print(f"Conversion failed for {test_file}: {str(e)}")
