import unittest
from unittest.mock import MagicMock
from domain.client.client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.reading_repository = MagicMock()
        self.reading_repository.get_median_consumption_by_client_id.return_value = 200
        self.client = Client(1, self.reading_repository)
        self.client.median_consumption = 100

    def test_update_median_consumption_reading_is_not_of_client(self):
        reading = MagicMock()
        reading.client_id = 2
        self.client.process_new_reading_signal(reading)
        self.assertEqual(self.client.median_consumption, 100)

    def test_update_median_consumption_reading_is_of_client(self):
        reading = MagicMock()
        reading.client_id = 1
        self.client.process_new_reading_signal(reading)
        self.assertEqual(self.client.median_consumption, 200)
