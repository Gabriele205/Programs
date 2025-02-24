from db_manager import test_connection
from finance_manager import add_transaction, view_transaction,delete_transaction, edit_transaction
from plot_manager import plot_data

if __name__ == '__main__':
  test_connection()

print('Welcome to Home Banking')
function = ('''Do you want to choose the function? 
            1. Add transaction
            2. Change transaction
            3. Delete transaction
            4. View transaction
            0. Exit
            ''')
print(function)

while True:
  option = input('')
  match option:
    case '1':
     if __name__ == '__main__':
       date = input('Enter the date of the transiction (YYYY-MM-DD):\n')
       transaction_type= input('Enter the type of transiction (income or expense):\n')
       category = input('Enter the category of transiction:\n')
       amount = float(input('enter the amount of transiction:\n'))

       add_transaction(date, transaction_type, category,amount)
       
    
    case '2':
      if __name__ == '__main__':
        transaction_id = input('Enter the id of the transaction you want to edit:\n')
        date = input('Enter the new date of the transaction (YYYY-MM-DD):\n')
        transaction_type = input('Enter the new type of transaction (income or expense):\n')
        category = input('Enter the new category of transaction:\n')
        amount = float(input('Enter the new amount of transaction:\n'))
        edit_transaction(transaction_id, date, transaction_type, category, amount)
        
        
    case '3':
      if __name__ == '__main__':
        transaction_id = int(input('Enter the id of the transiction you want to delete:\n'))
        delete_transaction(transaction_id)
        
        
    case'4':
      if __name__ == '__main__':
        view_transaction()
        plot_data()
      
        
    case '0':
      print('Exit program')
      break
      
    case _:
      print('Invalid option, please try again')