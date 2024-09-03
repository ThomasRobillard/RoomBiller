class Bill:
    def __init__(self, amount, category, date, user):
        self.amount = amount
        self.category = category
        self.date = date
        self.user = user

    def __str__(self):
        return f"{self.category} Bill of ${self.amount:.2f} on {self.date}, paid by {self.user.name}"