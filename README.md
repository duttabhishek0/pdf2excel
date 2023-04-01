# PDF to Excel Converter

This is a Python application that allows you to convert PDF files to Excel spreadsheets.

## Installation
There are two ways to use the application, either by using the release files or building it from source

### Using the release files

1. Download the latest release from the [release page](https://github.com/duttabhishek0/pdf2excel/releases/tag/v1.0.0)
2. Double-click the installer file and follow the prompts to install the application.

### Build from Source

Alternatively, you can build an executable using PyInstaller:
To build the application from source, follow these steps:

1. Clone the repository:

```
git clone https://github.com/your-username/pdf-to-excel.git
```

2. Navigate to the project directory:

```
cd pdf-to-excel
```

3. cd pdf-to-excel
```
pip install -r requirements.txt
```

4. Build the executable file using PyInstaller:
```
pyinstaller --onefile --windowed ui/main_window.py
```

5. Navigate to the `dist` folder and run the executable.


## Usage

1. Select a PDF file to convert by clicking the "Select File" button.
2. Choose an output directory for the converted file by clicking the "Select Output Directory" button.
3. Click the "Convert" button to convert the file.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`.
3. Make your changes and commit them: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
