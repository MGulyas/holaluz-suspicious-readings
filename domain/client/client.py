from blinker import signal


class Client:
    def __init__(self, id, reading_repository):
        self.id = id
        self.median_consumption = None
        self.reading_repository = reading_repository
        reading_added = signal('reading_added')
        reading_added.connect(self.process_new_reading_signal)

    def process_new_reading_signal(self, reading):
        if reading.client_id == self.id:
            self.median_consumption = self.reading_repository.get_median_consumption_by_client_id(self.id)
