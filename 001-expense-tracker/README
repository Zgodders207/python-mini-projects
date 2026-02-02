# Expense Tracker

A command-line tool to track expenses and understand your spending habits by category.

## Description

Tracking daily expenses manually is tedious, and it's easy to lose sight of where your money goes. This CLI tool makes it simple to log purchases, view spending history, and see totals by category — helping you stay on top of your budget.

With this tool you can:
- Add expenses with a name, amount, and category
- View all recorded expenses
- See your total spending
- View spending broken down by category (Food, Clothes, Bills, Rent)

## What I Learned

- **Lists**: Storing multiple expenses in a collection
- **Dictionaries**: Structuring each expense with key-value pairs (`name`, `amount`, `category`)
- **While loops**: Creating an interactive menu that runs until the user quits
- **For loops with `enumerate()`**: Displaying numbered category options
- **User input and validation**: Handling invalid input with try/except
- **Generator expressions**: Using `sum(expense['amount'] for expense in expenses)` to calculate totals

## How to Run

```bash
python expense_tracker.py
```

## Example Usage

```
 Expense Tracker
1. Add Expense
2. View Expenses
3. Total Spent
4. Spending by category
5. Quit
Choose an option: 1
Enter expense name: Coffee
Enter expense amount: 4.50
Categories:
1. Food
2. Clothes
3. Bills
4. Rent
Enter expense category: 1
Expense added.
```

## Future Improvements

- [ ] Save expenses to a JSON file so data persists between sessions
- [ ] Add ability to delete or edit expenses
- [ ] Let users add custom categories
- [ ] Filter expenses by date range
- [ ] Add input validation for expense amounts

## Reflection

This was my first Python project. I learned how lists and dictionaries work together to store structured data, and how to build an interactive menu using a while loop. The trickiest part was getting the index conversion right when displaying categories (adding 1 for display, subtracting 1 to access the list).
