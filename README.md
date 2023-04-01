# PDF to Excel Converter

[![Build Status](https://travis-ci.com/duttabhishek0/pdf2excel.svg?branch=main)](https://travis-ci.com/duttabhishek0/pdf2excel)
[![GitHub license](https://img.shields.io/github/license/duttabhishek0/pdf2excel)](https://github.com/duttabhishek0/pdf2excel/blob/main/LICENSE)


This is a Python application that allows you to convert PDF files to Excel spreadsheets.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Run the application: `python ui/main_window.py`

## Build from Source

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

## Test - Passing

If you are building from source, and have made some changes, make sure to run the tests once, to know if the changes made takes the application to a safe state or not. If the former happens, then it will pass the test, and the output will be like this:


![Screenshot from 2023-04-02 02-06-30](https://user-images.githubusercontent.com/56694152/229315310-49beeefb-d069-47b2-ae95-7aa2b0594426.png)
