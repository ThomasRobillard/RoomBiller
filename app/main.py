from .data.user import User
from .data.bill import Bill
from .data.split import Split
from .gui.mainframe import BudgetApp
from .data.storage import *
import tkinter as tk

def main():
    root = BudgetApp() # main application window

    
    
    root.mainloop()
# def add_bill(amount, category, date, user):
#     # This function will handle adding a bill to the appropriate user
#     print(f"Adding bill: {amount}, {category}, {date}, for {user}")
# Create users
user1 = User("Thomas")
user2 = User("Jordon")

# define split percentages
percentages = {
    user1: 50,
    user2: 50
}

# create new split
split = Split([user1, user2], percentages)

# Adding bills to split
bill1 = Bill(1210.0, "Rent", "2024-08-25")
split.add_bill(bill1, user1) # rent paid by Thomas (user1)
bill2 = Bill(94.92, "ALDI", "2024-08-12")
split.add_bill(bill2, user2) # aldi shopping paid by Jordon (user2)


# # Saving Data
# save_data([user1, user2])

# # Loading data
# loaded_users = load_data()
# for user in loaded_users:
#     print(user)
#     for bill in user.bills:
#         print(" ", bill)

# Calculate_imbalance
split.calculate_imbalance()

if __name__ == '__main__':
    main()