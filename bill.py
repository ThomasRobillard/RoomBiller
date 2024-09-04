class Bill:
    def __init__(self, amount, category, date, user):
        self.amount = amount
        self.category = category
        self.date = date
        self.user = user #test

    def __str__(self):
        return f"{self.category} Bill of ${self.amount:.2f} on {self.date}, paid by {self.user.name}"
    
    def calculate_imbalance(user1, user2):
        total_paid_user1 = user1.get_total_paid()
        total_paid_user2 = user2.get_total_paid()
        
        total_spent = total_paid_user1 + total_paid_user2
        should_have_paid_each = total_spent / 2
        
        imbalance_user1 = total_paid_user2 - should_have_paid_each
        imbalance_user2 = total_paid_user1 - should_have_paid_each
        
        if imbalance_user1 > 0:
            print(f"{user1.name} should pay {user2.name} ${imbalance_user1:.2f} to even out.")
        elif imbalance_user2 > 0:
            print(f"{user2.name} should pay {user1.name} ${imbalance_user2:.2f} to even out.")
        else:
            print("Both users are even.")
