import csv
from bill import *
from user import *

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