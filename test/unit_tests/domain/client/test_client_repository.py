import unittest
from unittest.mock import MagicMock

from domain.client.client_repository import ClientRepository


class TestClientRepository(unittest.TestCase):

    def setUp(self):
        self.client_repository = ClientRepository(MagicMock())
        self.client_repository.clients = {1: MagicMock(), 2: MagicMock()}

    def test_process_new_reading_signal_client_already_exists(self):
        reading = MagicMock()
        reading.client_id = 2
        self.client_repository.process_new_reading_signal(reading)
        self.assertTrue(reading.client_id in self.client_repository.clients)

    def test_process_new_reading_singal_new_client(self):
        reading = MagicMock()
        reading.client_id = 3
        self.client_repository.process_new_reading_signal(reading)
        self.assertTrue(reading.client_id in self.client_repository.clients)

    def test_get_client_by_id_does_not_exist(self):
        self.assertIsNone(self.client_repository.get_client_by_id(3))

    def test_get_client_by_id(self):
        self.assertIsNotNone(self.client_repository.get_client_by_id(1))
