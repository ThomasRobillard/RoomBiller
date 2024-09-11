class Split:
    def __init__(self, users, percentages):
        # Initializes a Split instance.
        # users: A list of User objects
        # percentages: A dictionary mapping users to their responsibility percentage (sum must equal 100)
        self.users = users
        self.percentages = percentages  # A dictionary of {User: Percentage}
        self.bills = []  # List of all shared bills

    def add_bill(self, bill, paying_user):
        # Adds a bill to the split and assigns it to the paying user.
        # bill: The Bill object to add
        # paying_user: The User who paid the bill
        bill.paying_user = paying_user
        self.bills.append(bill)
        paying_user.add_bill(bill)

    def calculate_split(self):
        # Calculates how much each user owes or is owed based on their responsibility percentages.
        total_spent = sum(bill.amount for bill in self.bills)
        user_totals = {user: 0 for user in self.users}

        # Calculate how much each user should have paid based on their percentage
        for user in self.users:
            should_have_paid = total_spent * (self.percentages[user] / 100)
            user_totals[user] = should_have_paid

        return user_totals

    def calculate_imbalance(self):
        # Calculates the imbalance between what each user paid and what they should have paid.
        user_totals = self.calculate_split()
        for user in self.users:
            actual_paid = user.total_paid
            should_have_paid = user_totals[user]
            imbalance = actual_paid - should_have_paid

            if imbalance > 0:
                print(f"{user.name} should receive ${imbalance:.2f}.")
            elif imbalance < 0:
                print(f"{user.name} owes ${abs(imbalance):.2f}.")
            else:
                print(f"{user.name} has paid the correct amount.")
