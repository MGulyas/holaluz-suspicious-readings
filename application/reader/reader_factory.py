from application.reader.csv_reader import CsvReader
from application.reader.xml_reader import XmlReader


class ReaderFactory:
    @staticmethod
    def get_reader(file_path):
        if file_path.endswith('.csv'):
            return CsvReader(file_path)
        elif file_path.endswith('.xml'):
            return XmlReader(file_path)
        else:
            raise ValueError('Unsupported file type')