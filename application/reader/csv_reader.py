import csv

from domain.reading.reading import Reading


class ReadingDTO:
    def __init__(self, client, period, reading):
        self.client = client
        self.period = period
        self.reading = reading

    def from_dto(self, client_repository):
        return Reading(self.client, self.period, float(self.reading), client_repository)


class CsvReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            # Skip first row
            next(reader)
            return [ReadingDTO(row[0], row[1], row[2]) for row in reader]
