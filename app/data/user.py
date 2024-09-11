from app.data.bill import Bill

class User:
    def __init__(self, name):
        self.name = name
        self.total_paid = 0.0 # Total amount user has paid
        self.bills = [] # list of every bill user has paid
    
    def add_bill(self, bill):
        self.bills.append(bill)
        self.total_paid += bill.amount

    def __str__(self):
        return f"User: {self.name}, Total Paid: ${self.total_paid:.2f}"
    
    # def get_total_paid(self):
    #     return self.total_paid
    