# empty dictionary list to store expenses
expenses = []
categories = ["Food", "Clothes", "Bills", "Rent"]

while True:
    print("\n Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Spending by category")
    print("5. Quit")
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter expense name:")
        amount = input("Enter expense amount:")
        category = ""
        while True:
            print("Categories:")
            for index, item in enumerate(categories):
                print(f"{index+1}. {item}")
            category_num = input("Enter expense category:")
            if int(category_num) < 0 or int(category_num) > len(categories):
                print("Invalid Option. Try again!")
            else:
                category = categories[int(category_num)+1]
                break

        expense = {
            'name': name,
            'amount': float(amount),
            'category': category
        }
        expenses.append(expense)
        print("Expense added.")

    elif choice == '2':
        for expense in expenses:
            print(f"Name: {expense['name']} | Amount: {expense['amount']} | Category: {expense['category']}")


    elif choice == '3':
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total spent: {total}")

    elif choice == '4':
        for item in categories:
            category_total = 0
            for expense in expenses:
                if expense['category'] == item:
                    category_total += expense['amount']
            print(f"{item}: £{category_total}")

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.")



