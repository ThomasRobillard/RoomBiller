import csv
from app.data.bill import *
from app.data.user import *
from app.data.split import Split

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
    
def export_split_data(split, filename='split_data.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['type', 'name', 'amount', 'category', 'date', 'percentage', 'payer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        # Export user data and their total paid
        for user in split.users:
            writer.writerow({
                'type': 'user',
                'name': user.name,
                'amount': user.total_paid
            })

        # Export percentages of responsibility for each user
        for user, percentage in split.percentages.items():
            writer.writerow({
                'type': 'percentage',
                'name': user.name,
                'percentage': percentage
            })

        # Export bill data and which user paid
        for bill in split.bills:
            writer.writerow({
                'type': 'bill',
                'amount': bill.amount,
                'category': bill.category,
                'date': bill.date,
                'payer': bill.paying_user.name  # Assuming paying_user is an attribute of the Bill class
            })

def load_split_data(filename='split_data.csv'):
    users = {}
    percentages = {}
    bills = []
    
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['type'] == 'user':
                    # Reconstruct user objects and set their total paid
                    name = row['name']
                    total_paid = float(row['amount'])
                    user = User(name)
                    user.total_paid = total_paid  # Assign the total paid amount directly
                    users[name] = user

                elif row['type'] == 'percentage':
                    # Assign percentage responsibilities
                    name = row['name']
                    percentage = float(row['percentage'])
                    percentages[users[name]] = percentage

                elif row['type'] == 'bill':
                    # Reconstruct bill objects, but don't add it to the user's bills again
                    amount = float(row['amount'])
                    category = row['category']
                    date = row['date']
                    payer_name = row['payer']
                    bill = Bill(amount, category, date, users[payer_name])
                    bills.append(bill)

        # Create a Split instance and return it
        split = Split(list(users.values()), percentages)
        split.bills = bills  # Assign the loaded bills to the split, but don't modify user totals
        return split

    except FileNotFoundError:
        print("File not found.")
        return None