class TrackerType:
    def __init__(self, in_ex_inv, name):
        self.in_ex_inv = in_ex_inv  # Income, Expense or Investment
        self.name = name
        self.total = 0

        # print("Type '{}' created as {}!".format(self.name, self.in_ex_inv))

    def __str__(self):
        return self.name

    def sum(self, amount):
        self.total += amount

    def get_total(self):
        return round(self.total, 2)