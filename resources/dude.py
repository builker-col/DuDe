from PIL import Image
import pytesseract
import os

class DuDe:
    def __init__(self, data_dir):
        """
        Initializes a new instance of the DuDe class.

        Parameters:
        data_dir (str): The directory path where the data files are located.

        Attributes:
        hash_map (dict): A dictionary to store file hashes as keys and file paths as values.
        duplicates (dict): A dictionary to store duplicate file hashes as keys and lists of file paths as values.
        data_dir (str): The directory path where the data files are located.
        list_of_files (list): A list of file names in the data directory.
        """
        self.hash_map = {}
        self.duplicates = {}
        self.data_dir = data_dir
        self.list_of_files = os.listdir(data_dir)

    def ocr_core(self, filename):
        """
        Perform OCR (Optical Character Recognition) on an image file.

        Parameters:
        - filename (str): The path to the image file.

        Returns:
        - text (str): The extracted text from the image.
        """
        text = pytesseract.image_to_string(Image.open(filename))
        return text

    def find_duplicates(self, num_initial_chars=2):
        """
        Finds and identifies duplicate files based on the initial characters of their text content.

        Args:
            num_initial_chars (int): The number of initial characters to consider for comparison. Defaults to 2.

        Returns:
            None
        """
        for file in self.list_of_files:
            file_path = os.path.join(self.data_dir, file)
            text = self.ocr_core(file_path)
            initial = text[:num_initial_chars]

            if initial in self.hash_map:
                for files_same_initial in self.hash_map[initial]:
                    file_text = self.ocr_core(os.path.join(self.data_dir, files_same_initial))
                    if file_text[:50] == text[:50]:
                        self.duplicates.setdefault(files_same_initial, []).append(file)
                self.hash_map[initial].append(file)
            else:
                self.hash_map[initial] = [file]

    def get_duplicates(self) -> dict:
            """
            Returns a dictionary containing the duplicates found.

            Returns:
                dict: A dictionary where the keys are the duplicate items and the values are the number of occurrences.
            """
            return self.duplicates

    def get_hash_map(self) -> dict:
            """
            Returns the hash map associated with the object.

            Returns:
                dict: The hash map associated with the object.
            """
            return self.hash_map
