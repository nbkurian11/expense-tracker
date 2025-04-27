
from income import Income
from expense import Expense

if __name__ == '__main__':
    monthly_income = input("What is your monthly income?")
    monthly_income = float(monthly_income)

    user_income = Income(monthly_income)

    choice = input("Do you want to add a monthy expense? (yes/no)")

    total_expenses = []

    while choice == "yes":
        expense_type = input("What is the expense type? (Rent, Food, Gym, etc.)")
        expense_amount = input("What is the expense amount?")
        user_expense = Expense(expense_type, float(expense_amount))
        total_expenses.append(user_expense)
        choice = input("Do you want to add an another monthly expense? (yes/no)")
        
        
    print("Total Expenses: ")
    for expense in total_expenses:
        print(f"{expense.expense_type}: ${expense.amount}")

    total_amount = 0
    for expense in total_expenses:
        total_amount += expense.amount


    leftover = monthly_income - total_amount

    print("You have $" + str(leftover) +"leftover.")

    




        
    

    
    
    
    
    
    
    
    
    
    
    

   
    
