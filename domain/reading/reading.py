class Reading:
    def __init__(self, client_id, period, consumption, client_repository):
        self.client_id = client_id
        self.period = period
        self.consumption = consumption
        self.client_repository = client_repository

    def __eq__(self, other):
        return self.client_id == other.client_id and self.period == other.period and self.consumption == other.consumption

    def is_suspicious(self):
        client_median_consumption = self.client_repository.get_client_by_id(self.client_id).median_consumption
        return self.consumption > 1.5 * client_median_consumption or self.consumption < 0.5 * client_median_consumption
