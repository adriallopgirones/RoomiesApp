class GroupManager():
    def __init__(self):
        self.users = []
        self.purchases = []
        self.group_id = ""

    def update_group(self, users, purchases, group_id):
        self.users = users
        self.purchases = purchases
        self.group_id = group_id

    def build_debts_table(self):
        debts_table = {}
        for user in self.users:
            debts_table[user.username] = user.debt

        return debts_table
