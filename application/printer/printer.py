from tabulate import tabulate


class ReadingWithMedianDTO:
    def __init__(self, client_id, period, consumption, median):
        self.client_id = client_id
        self.period = period
        self.consumption = consumption
        self.median = median


class Printer:
    def print(self, readings_with_medians):
        table = [['Client', 'Month', 'Suspicious', 'Median']]
        for reading_with_median in readings_with_medians:
            table.append([reading_with_median.client_id, reading_with_median.period, reading_with_median.consumption,
                          reading_with_median.median])
        print(tabulate(table, headers='firstrow'))
