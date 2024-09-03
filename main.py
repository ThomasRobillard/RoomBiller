from user import User
from bill import Bill
import csv

def save_data(users, filename='budget_data.csv'):
    with open(filename, 'w', newline = '') as csvfile:
        fieldnames = ['name', 'amount', 'category', 'date']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        writer.writeheader()
        for user in users:
            for bill in user.bills:
                writer.writerow({'name': bill.user.name, 'amount': bill.amount, 'category': bill.category, 'date': bill.date})

def load_data(filename='budget_data.csv'):
    users = {}

    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                if name not in users:
                    users[name] = User(name)
                bill = Bill(float(row['amount']), row['category'], row['date'], users[name])
                users[name].add_bill(bill.amount, bill.category, bill.date)
        return list(users.values())
    except FileNotFoundError:
        return []

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



# Saving Data
save_data([user1, user2])

# Loading data
loaded_users = load_data()
for user in loaded_users:
    print(user)
    for bill in user.bills:
        print(" ", bill)

# Calculate imbalance
calculate_imbalance(loaded_users[0], loaded_users[1])
print("Jordon overpaid last month by $383.46, which was not factored in.")
