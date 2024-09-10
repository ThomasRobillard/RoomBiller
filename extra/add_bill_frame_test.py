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