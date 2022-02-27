months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']


class AnnualTracker:
    def __init__(self, year):
        self.year = year
        self.trackers = []

    def add(self, tracker):
        self.trackers.append(tracker)

    def total_incomes(self):
        total = 0
        for tracker in self.trackers:
            total += tracker.total_incomes()
        return round(total, 2)

    def total_expenses(self):
        total = 0
        for tracker in self.trackers:
            total += tracker.total_expenses()
        return round(total, 2)

    def total_investments(self):
        total = 0
        for tracker in self.trackers:
            total += tracker.total_investments()
        return round(total, 2)

    def balance(self):
        return round(self.total_incomes() - self.total_expenses() - self.total_investments(), 2)
