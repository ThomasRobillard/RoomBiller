from app.data.user import User
from app.data.bill import Bill
from app.data.storage import *
import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Budgeting Application')
    root.geometry('600x400')  # Set the size of the window

    
    
    root.mainloop()
def add_bill(amount, category, date, user):
    # This function will handle adding a bill to the appropriate user
    print(f"Adding bill: {amount}, {category}, {date}, for {user}")
# Create users
user1 = User("Thomas")
user2 = User("Jordon")

# Adding bills
user1.add_bill(1210.0, "Rent", "2024-08-25")
user1.add_bill(56.99, "Internet", "2024-08-22")
user1.add_bill(6.37, "Insurance", "2024-08-22")
user1.add_bill(129.9, "Electric", "2024-09-04")

user2.add_bill(94.92, "ALDI", "2024-08-12")
user2.add_bill(81.92, "Walmart", "2024-08-12")
user2.add_bill(99.52, "ALDI", "2024-08-19")
user2.add_bill(48.96, "Walmart", "2024-08-19")
user2.add_bill(114.00, "Goodwill", "2024-08-22")
user2.add_bill(87.42, "Walmart", "2024-08-22")
user2.add_bill(136.53, "Walmart", "2024-09-02")
user2.add_bill(160.00, "ALDI", "2024-09-02")



# Saving Data
save_data([user1, user2])

# Loading data
loaded_users = load_data()
for user in loaded_users:
    print(user)
    for bill in user.bills:
        print(" ", bill)

# Calculate_imbalance
Bill.calculate_imbalance(loaded_users[0], loaded_users[1])

if __name__ == '__main__':
    main()