import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdf-to-excel",
    version="1.0.0",
    author="Abhishek Dutt",
    author_email="duttabhishek0@gmail.com",
    description="A desktop application to convert PDF files to Excel files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/duttabhishek0/pdf2excel/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pdfminer.six",
        "openpyxl",
        "PyQt5",
    ],
    entry_points={
        "gui_scripts": [
            "pdf-to-excel=pdf_to_excel.ui:main_window"
        ]
    },
    package_data={
        "pdf_to_excel": ["resources/*"]
    },
)
