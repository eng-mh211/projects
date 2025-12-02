import datetime
import calendar
from expense import Expense

budget = 2000

def main():
    print("Running")
    expense_file_path ="data.csv"

    # input from user
    exp = get_user_data()

    # save there data to a file
    save_user_data(exp, expense_file_path)
    # read file and summarize
    read_user_data(expense_file_path,budget)

    pass


def get_user_data():
    print("getting user expense")
    ex_name = input("enter expanse name: ")
    ex_amount = float(input("enter expanse amount: "))
    print(f"you entered: {ex_name}")
    print(f"you entered: {ex_amount}")

    expense_cat = [
        "Food", "Home", "Work", "Fun", "Mice"
    ]

    while True:
        print("select the expense category:")
        for i, category_name in enumerate(expense_cat):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1-{len(expense_cat)}]"
        select_index = int(input(f"enter a category number {value_range}: ")) - 1

        if select_index in range(len(expense_cat)):
            select_category = expense_cat[select_index]
            new_expense = Expense(name= ex_name,category= select_category,amount= ex_amount)
            return new_expense
        else:
            print("invalid input")

def save_user_data(exp,expense_file_path):
    print(f"saving user expense:  {exp}")
    with open(expense_file_path,"a") as f:
        f.write(f"{exp.name},{exp.category},{exp.amount}\n")

def read_user_data(expense_file_path, budget):
    print("reading user expense")
    expenses =[]
    with open(expense_file_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            ex_name ,select_category ,ex_amount = line.strip().split(",")
            line_expense = Expense(name=ex_name,category=select_category,amount=float(ex_amount))
            expenses.append(line_expense)


    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] =expense.amount

    print("Expenses By Category:")
    for key, amount in amount_by_category.items():
        print(f' {key}: ${amount:.2f}')

    total_spent = sum(e.amount for e in expenses)
    print(f"total spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"remaining budget: ${remaining_budget:.2f}")





if __name__ == '__main__':
    main()
    pass
