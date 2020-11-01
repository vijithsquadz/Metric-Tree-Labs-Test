import fitz
import json
import os


class PDFReader:

    def __init__(self, path):
        self.file_path = path

    def read(self):
        if not os.path.exists(self.file_path):
            raise Exception("Input file does not exists !!!")

        with fitz.open(self.file_path) as pdf_doc:
            content = ""
            for page in pdf_doc:
                content += page.getText().strip()

        return content


class JSONWriter:

    def __init__(self, path):
        self.file_path = path

    def write(self, dict_content):
        with open(self.file_path, "w", encoding='utf-8') as outfile:
            json.dump(dict_content, outfile, indent=2, ensure_ascii=False)
