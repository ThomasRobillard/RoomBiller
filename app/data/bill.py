class Bill:
    def __init__(self, amount, category, date, paying_user=None):
        self.amount = amount
        self.category = category
        self.date = date
        self.paying_user = paying_user

    def __str__(self):
        return f"{self.category} Bill of ${self.amount:.2f} on {self.date}, paid by {self.paying_user.name if self.paying_user else 'Unknown'}"