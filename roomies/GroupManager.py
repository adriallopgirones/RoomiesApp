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

    def update_debts_edit_purchase(self, purchase_id, prior_purchase):
        debts_table = self.build_debts_table()
        edited_purchased = [p for p in self.purchases if p.id == purchase_id][0]
        debts_table[prior_purchase.user.username] -= prior_purchase.product_price
        debts_table[edited_purchased.user.username] += edited_purchased.product_price
        for receiver in eval(prior_purchase.receivers):
            debts_table[receiver] += prior_purchase.product_price / len(eval(prior_purchase.receivers))
        for receiver in eval(edited_purchased.receivers):
            debts_table[receiver] -= edited_purchased.product_price / len(eval(edited_purchased.receivers))

        return debts_table

    def update_debts_pay_purchase(self, purchase_id):
        debts_table = self.build_debts_table()
        new_purchase = [p for p in self.purchases if p.id == purchase_id][0]
        debts_table[new_purchase.user.username] += new_purchase.product_price
        for receiver in eval(new_purchase.receivers):
            debts_table[receiver] -= new_purchase.product_price / len(eval(new_purchase.receivers))

        return debts_table



