import pandas as pd

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']


class MonthlyTracker:
    def __init__(self, month, year):
        self.month = months[month - 1]
        self.year = year
        self.incomes = pd.DataFrame(
            {
                'Description': [],
                'Type': [],
                'Amount': [],
            }
        )

        self.expenses = pd.DataFrame(
            {
                'Description': [],
                'Type': [],
                'Amount': [],
            }
        )

        self.investments = pd.DataFrame(
            {
                'Description': [],
                'Type': [],
                'Amount': [],
            }
        )

        # print("New Expense_Tracker for {}, {} created".format(self.month, self.year))

    def income(self, description, type, amount):
        if type.in_ex_inv == 'Income':
            type.sum(amount)
            new_income = pd.DataFrame({'Description': [description], 'Type': [type.name], 'Amount': [amount]})
            self.incomes = pd.concat([self.incomes, new_income], ignore_index=True)
        else:
            print('Error, check type definition or declaration')

    def expense(self, description, type, amount):
        if type.in_ex_inv == 'Expense':
            type.sum(amount)
            new_expense = pd.DataFrame({'Description': [description], 'Type': [type.name], 'Amount': [amount]})
            self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
        else:
            print('Error, check type definition or declaration')

    def investment(self, description, type, amount):
        if type.in_ex_inv == 'Investment':
            type.sum(amount)
            new_investment = pd.DataFrame({'Description': [description], 'Type': [type.name], 'Amount': [amount]})
            self.investments = pd.concat([self.investments, new_investment], ignore_index=True)
        else:
            print('Error, check type definition or declaration')

    def multiple_incomes(self, incomes):
        for inc in incomes:
            self.income(inc[0], inc[1], inc[2])

    def multiple_expenses(self, expenses):
        for exp in expenses:
            self.expense(exp[0], exp[1], exp[2])

    def multiple_investments(self, investments):
        for inv in investments:
            self.investment(inv[0], inv[1], inv[2])

    def total_incomes(self):
        total = 0
        for index, value in self.incomes['Amount'].items():
            total += value
        return round(total, 2)

    def total_expenses(self):
        total = 0
        for index, value in self.expenses['Amount'].items():
            total += value
        return round(total, 2)

    def total_investments(self):
        total = 0
        for index, value in self.investments['Amount'].items():
            total += value
        return round(total, 2)

    def balance(self):
        return round(self.total_incomes() - self.total_expenses() - self.total_investments(), 2)
