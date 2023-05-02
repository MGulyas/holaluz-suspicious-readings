import unittest
from unittest.mock import MagicMock
from domain.reading.reading import Reading


class TestReading(unittest.TestCase):

    def setUp(self):
        client = MagicMock()
        client.median_consumption = 100
        self.client_repository = MagicMock()
        self.client_repository.get_client_by_id.return_value = client

    def test_is_suspicious(self):
        suspicious_readings = [Reading(1, 1, 151, self.client_repository), Reading(1, 1, 2000, self.client_repository),
                               Reading(1, 1, 49, self.client_repository), Reading(1, 1, 0, self.client_repository)]

        for reading in suspicious_readings:
            self.assertEqual(True, reading.is_suspicious())

    def test_is_not_suspicious(self):
        ok_readings = [Reading(1, 1, 100, self.client_repository), Reading(1, 1, 101, self.client_repository),
                       Reading(1, 1, 99, self.client_repository), Reading(1, 1, 51, self.client_repository),
                       Reading(1, 1, 149, self.client_repository)]

        for reading in ok_readings:
            self.assertEqual(False, reading.is_suspicious())
