import numpy as np
from blinker import signal


class ReadingRepository:
    def __init__(self):
        self.readings = []

    def add_readings(self, readings):
        self.readings.extend(readings)
        reading_added = signal('reading_added')
        for reading in readings:
            reading_added.send(reading)

    def get_all_suspicious_readings(self):
        return [reading for reading in self.readings if
                reading.is_suspicious()]

    def get_median_consumption_by_client_id(self, client_id):
        if not self.readings:
            return None

        readings_by_client = [reading.consumption for reading in self.readings if reading.client_id == client_id]

        if not readings_by_client:
            return None

        return np.median(readings_by_client)
