from application.printer.printer import Printer, ReadingWithMedianDTO
from application.reader.reader_factory import ReaderFactory
from infrastructure.index import reading_repository, client_repository


def add_readings_from_file(filename):
    reader = ReaderFactory.get_reader(filename)
    reading_dtos = reader.read()
    readings = [reading_dto.from_dto(client_repository) for reading_dto in reading_dtos]
    reading_repository.add_readings(readings)


def print_suspicious_readings():
    suspicious_readings = reading_repository.get_all_suspicious_readings()
    suspicious_readings_with_medians = [
        ReadingWithMedianDTO(reading.client_id, reading.period, reading.consumption,
                             client_repository.get_client_by_id(reading.client_id).median_consumption) for reading in
        suspicious_readings]
    printer = Printer()
    printer.print(suspicious_readings_with_medians)
