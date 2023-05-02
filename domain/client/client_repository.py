from blinker import signal

from domain.client.client import Client


class ClientRepository:
    def __init__(self, reading_repository):
        self.clients = dict()
        self.reading_repository = reading_repository
        reading_added = signal('reading_added')
        reading_added.connect(self.process_new_reading_signal)

    def process_new_reading_signal(self, reading):
        if reading.client_id not in self.clients:
            self.clients[reading.client_id] = Client(reading.client_id, self.reading_repository)

    def get_client_by_id(self, client_id):
        if client_id not in self.clients:
            return None
        return self.clients[client_id]
