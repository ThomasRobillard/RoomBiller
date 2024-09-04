from user import User
from bill import Bill
from data import *
import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Budgeting Application')
    root.geometry('600x400')  # Set the size of the window

    # Add more components here
    def add_bill_frame(root):
        frame = tk.Frame(root)
        frame.pack(pady=20)

    # Amount Entry
        tk.Label(frame, text="Amount:").grid(row=0, column=0)
        amount_entry = tk.Entry(frame)
        amount_entry.grid(row=0, column=1)

        # Category Entry
        tk.Label(frame, text="Category:").grid(row=1, column=0)
        category_entry = tk.Entry(frame)
        category_entry.grid(row=1, column=1)

        # Date Entry
        tk.Label(frame, text="Date:").grid(row=2, column=0)
        date_entry = tk.Entry(frame)
        date_entry.grid(row=2, column=1)

        # User Selection
        tk.Label(frame, text="User:").grid(row=3, column=0)
        user_var = tk.StringVar(frame)
        user_var.set("Choose a User")  # default value
        user_dropdown = tk.OptionMenu(frame, user_var, "Alice", "Bob")
        user_dropdown.grid(row=3, column=1)

        # Submit Button
        submit_button = tk.Button(frame, text="Add Bill", command=lambda: add_bill(amount_entry.get(), category_entry.get(), date_entry.get(), user_var.get()))
        submit_button.grid(row=4, columnspan=2)

        return frame
    add_bill_frame(root)
    
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
user1.add_bill(0.00, "Electric", "2024-08-22")

user2.add_bill(94.92, "ALDI", "2024-08-12")
user2.add_bill(81.92, "Walmart", "2024-08-12")
user2.add_bill(99.52, "ALDI", "2024-08-19")
user2.add_bill(48.96, "Walmart", "2024-08-19")
user2.add_bill(114.00, "Goodwill", "2024-08-22")
user2.add_bill(87.42, "Walmart", "2024-08-22")
user2.add_bill(136.53, "Walmart", "2024-09-02")
user2.add_bill(160.00, "ALDI", "2024-09-02")



# # Saving Data
# save_data([user1, user2])

# # Loading data
# loaded_users = load_data()
# for user in loaded_users:
#     print(user)
#     for bill in user.bills:
#         print(" ", bill)

# Calculate imbalance
# calculate_imbalance(loaded_users[0], loaded_users[1])

if __name__ == '__main__':
    main()