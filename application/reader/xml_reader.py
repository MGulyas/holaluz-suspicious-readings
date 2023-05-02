from domain.reading.reading import Reading
import xml.etree.ElementTree as ET


class ReadingDTO:
    def __init__(self, client, period, reading):
        self.client = client
        self.period = period
        self.reading = reading

    def from_dto(self, client_repository):
        return Reading(self.client, self.period, float(self.reading), client_repository)


class XmlReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        root = ET.parse(self.file_path).getroot()
        return [ReadingDTO(reading.attrib['clientID'], reading.attrib['period'], reading.text) for reading in root]
