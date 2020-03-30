class GroupManager():
    def __init__(self):
        self.users = []
        self.purchases = []
        self.group_id = ""

    def update_group(self, users, purchases, group_id):
        self.users = users
        self.purchases = purchases
        self.group_id = group_id

    def build_debts_table(self, intern = False):
        debts_table = {}
        if intern:
            for user in self.users:
                debts_table[user.username] = 0
            return debts_table
        else:
            for user in self.users:
                debts_table[user.username] = user.debt
            return debts_table

    def update_debts(self):
        debts_table = self.build_debts_table(intern = True)
        for p in self.purchases:
            if p.purchased:
                debts_table[p.user.username] += p.product_price
                for receiver in eval(p.receivers):
                    debts_table[receiver] -= p.product_price / len(eval(p.receivers))

        return debts_table




