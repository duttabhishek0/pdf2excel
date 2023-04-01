import logging
import os
import sys
import time
import unittest

from pdf_to_excel.conversion import convert_pdf_to_excel


class TestConversion(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "test_data"
        )
        self.test_output_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "test_output"
        )
        if not os.path.exists(self.test_output_dir):
            os.makedirs(self.test_output_dir)

    def test_conversion(self):
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
                logging.info(f"Conversion successful for {test_file}")
                print(f"Conversion successful for {test_file}")
            except Exception as e:
                logging.exception(f"Conversion failed for {test_file}")
                print(f"Conversion failed for {test_file}: {str(e)}")

if __name__ == "__main__":
    # set up logging
    log_file_name = time.strftime("admin.log")
    logging.basicConfig(filename=log_file_name, level=logging.DEBUG)
    # set up console output
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
    # run tests
    unittest.main()
