import json
from datetime import date

curr_month = {}
curr_expense = {}

def welcome_message():
    print("Welcome to Financial Watch!")

def command_message():
    print("Enter a command")
    print("0 = end program")
    print("1 = add expense")

def userInput():
    return input()

def add_expense():
    today = date.today()
    print("Expense cost:")
    expense_cost = input()
    print("Expense type")
    expense_type = input()
    print("Expense day dd")
    expense_date = input()

    new_expense = {'cost': expense_cost, 'type': expense_type, 'date': (expense_date + "-" + today.strftime("%m-%y"))}
    expense_len = len(curr_expense)
    if expense_len == 0:
        curr_expense[expense_len] = new_expense
    else:
        curr_expense[expense_len+1] = new_expense

    # if len(curr_month)
    # curr_month[0] = curr_expense
    # print("add this okay: ", (expense_len), "---")
    # curr_expejnse[len] = new_expense

    print(new_expense)



def setup():
    curr_month[0] = curr_expense

setup();

welcome_message()
#Begin program
while 1:
    print(len(curr_expense))
    print(type(curr_month))
    command_message()
    curInput = userInput()
    print("Users input is: " + curInput)
    if curInput == "0":
        exit(1)
    if curInput == "1":
        add_expense()
    print(curr_month)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
