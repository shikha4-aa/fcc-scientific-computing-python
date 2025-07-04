class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)
            amt = f"{entry['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    spends = []

    # Get spending per category
    for category in categories:
        spend = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spends.append(spend)

    total_spend = sum(spends)
    percentages = [int((spend / total_spend) * 10) * 10 for spend in spends]

    # Chart bar levels
    for level in range(100, -1, -10):
        output += str(level).rjust(3) + '|'
        for percent in percentages:
            output += ' o ' if percent >= level else '   '
        output += ' \n'

    output += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    # Longest name for vertical writing
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        output += '     '
        for category in categories:
            if i < len(category.name):
                output += category.name[i] + '  '
            else:
                output += '   '
        output += '\n'

    return output.rstrip('\n')
