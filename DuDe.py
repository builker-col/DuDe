from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import json
import os

class DuDe:
    def __init__(self, data_dir):
        self.hash_map = {}
        self.duplicates = {}
        self.data_dir = data_dir
        self.list_of_files = os.listdir(data_dir)

    def ocr_core(self, filename):
        text = pytesseract.image_to_string(Image.open(filename))
        return text

    def find_duplicates(self):
        for file in self.list_of_files:
            file_path = os.path.join(self.data_dir, file)
            text = self.ocr_core(file_path)
            initial = text[:2]

            if initial in self.hash_map:
                for files_same_initial in self.hash_map[initial]:
                    file_text = self.ocr_core(os.path.join(self.data_dir, files_same_initial))
                    if file_text[:50] == text[:50]:
                        self.duplicates.setdefault(files_same_initial, []).append(file)
                self.hash_map[initial].append(file)
            else:
                self.hash_map[initial] = [file]

    def get_duplicates(self):
        return json.dumps(self.duplicates, indent=4)

    def get_hash_map(self):
        return json.dumps(self.hash_map, indent=4)