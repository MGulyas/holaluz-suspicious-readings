import unittest
from unittest.mock import MagicMock

from blinker import signal

from domain.reading.reading import Reading
from domain.reading.reading_repository import ReadingRepository


class MockReadingSignalSubscriber:
    def __init__(self):
        self.received_signals = []

    def process(self, reading):
        self.received_signals.append(reading)


class TestReading(unittest.TestCase):

    def setUp(self):
        self.client_repository = MagicMock()

    def test_add_one_reading(self):
        reading = Reading(1, 1, 100, self.client_repository)
        reading_repository = ReadingRepository()
        reading_repository.add_readings([reading])
        self.assertEqual(reading, reading_repository.readings[0])

    def test_add_two_readings(self):
        readings = [Reading(1, 1, 100, self.client_repository), Reading(1, 2, 100, self.client_repository)]
        reading_repository = ReadingRepository()
        reading_repository.add_readings(readings)
        for i in range(2):
            self.assertEqual(readings[i], reading_repository.readings[i])

    def test_add_one_reading_raises_domain_event(self):
        reading_added = signal('reading_added')
        subscriber = MockReadingSignalSubscriber()
        reading_added.connect(subscriber.process)

        reading = Reading(1, 1, 100, self.client_repository)
        reading_repository = ReadingRepository()
        reading_repository.add_readings([reading])
        self.assertEqual(reading, subscriber.received_signals[0])

    def test_add_two_readings_raises_two_domain_events(self):
        reading_added = signal('reading_added')
        subscriber = MockReadingSignalSubscriber()
        reading_added.connect(subscriber.process)

        reading_repository = ReadingRepository()
        reading_repository.add_readings(
            [Reading(1, 1, 100, self.client_repository), Reading(1, 1, 100, self.client_repository)])
        self.assertEqual(2, len(subscriber.received_signals))

    def test_get_all_suspicious_readings_no_readings(self):
        reading_repository = ReadingRepository()
        self.assertEqual([], reading_repository.get_all_suspicious_readings())

    def test_get_all_suspicious_readings_all_readings_suspicious(self):
        readings = [Reading(1, 1, 2000, self.client_repository), Reading(1, 1, 2, self.client_repository)]
        for reading in readings:
            reading.is_suspicious = MagicMock(return_value=True)
        reading_repository = ReadingRepository()
        reading_repository.add_readings(readings)
        self.assertEqual(readings, reading_repository.get_all_suspicious_readings())

    def test_get_all_suspicious_readings_some_readings_suspicious(self):
        readings = [Reading(1, 1, 2000, self.client_repository), Reading(1, 1, 102, self.client_repository),
                    Reading(1, 1, 2, self.client_repository)]
        readings[0].is_suspicious = MagicMock(return_value=True)
        readings[1].is_suspicious = MagicMock(return_value=False)
        readings[2].is_suspicious = MagicMock(return_value=True)
        reading_repository = ReadingRepository()
        reading_repository.add_readings(readings)
        self.assertEqual([readings[0], readings[2]], reading_repository.get_all_suspicious_readings())

    def test_get_all_suspicious_readings_no_readings_suspicious(self):
        readings = [Reading(1, 1, 101, self.client_repository), Reading(1, 1, 102, self.client_repository),
                    Reading(1, 1, 120, self.client_repository)]
        for reading in readings:
            reading.is_suspicious = MagicMock(return_value=False)
        reading_repository = ReadingRepository()
        reading_repository.add_readings(readings)
        self.assertEqual([], reading_repository.get_all_suspicious_readings())

    def test_get_median_consumption_by_client_id_no_readings_for_client(self):
        # TODO: should raise exception
        readings = [Reading(1, 1, 101, self.client_repository), Reading(1, 1, 102, self.client_repository),
                    Reading(1, 1, 120, self.client_repository),
                    Reading(2, 1, 201, self.client_repository), Reading(2, 1, 240, self.client_repository),
                    Reading(2, 1, 409, self.client_repository)]
        reading_repository = ReadingRepository()
        reading_repository.add_readings(readings)
        self.assertEqual(None, reading_repository.get_median_consumption_by_client_id(3))

    def test_get_median_consumption_by_client_id(self):
        readings = [Reading(1, 1, 101, self.client_repository), Reading(1, 1, 102, self.client_repository),
                    Reading(1, 1, 120, self.client_repository),
                    Reading(2, 1, 201, self.client_repository), Reading(2, 1, 240, self.client_repository),
                    Reading(2, 1, 409, self.client_repository)]
        reading_repository = ReadingRepository()
        reading_repository.add_readings(readings)
        self.assertEqual(102, reading_repository.get_median_consumption_by_client_id(1))
