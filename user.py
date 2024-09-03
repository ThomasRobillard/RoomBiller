from bill import Bill

class User:
    def __init__(self, name):
        self.name = name
        self.total_paid = 0.0
        self.bills = []
    
    def add_bill(self, amount, category, date):
        bill = Bill(amount, category, date, self)
        self.bills.append(bill)
        self.total_paid += amount

    def __str__(self):
        return f"User: {self.name}, Total Paid: ${self.total_paid:.2f}"
    
    def get_total_paid(self):
        return self.total_paid
    