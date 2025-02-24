from db_manager import get_connection
from tabulate import tabulate

def add_transaction (date, transaction_type, category, amount:float):
  try:
    connection = get_connection()
    if connection:
      cursor = connection.cursor()
      query = 'insert into transaction (date,transaction_type,category,amount) values (%s, %s, %s, %s)'
      cursor.execute(query,(date,transaction_type,category,amount))
    connection.commit()
    print('Transaction added successfully')
  except Exception as e:
    print(f'Error while adding transaction:{e}')
  finally:
    if connection:
      connection.close()




def edit_transaction(transaction_id:int, date, transaction_type, category, amount:float):
  try:
    connection = get_connection()
    if connection: 
      cursor = connection.cursor()
      query = 'update transaction set date = %s, transaction_type = %s, category = %s, amount = %s where id = %s'
      cursor.execute(query, (date,transaction_type, category, amount, transaction_id))
      connection.commit()
      print('Transaction updated successfully')
  except Exception as e:
      print(f'Error while deleting transaction: {e}')
  finally:
        if connection:
            connection.close()




def delete_transaction(transaction_id:int):
  try:
    connection = get_connection()
    if connection:
          cursor = connection.cursor()
          query = 'delete from transaction where id = %s'
          cursor.execute(query, (transaction_id,))
          connection.commit()
          print('Transaction deleted successfully')
  except Exception as e:
      print(f'Error while deleting transaction: {e}')
  finally:
        if connection:
            connection.close()




def view_transaction ():
  try:
    connection = get_connection()
    if connection:
      cursor = connection.cursor()
      cursor.execute('select * from transaction')
      results = cursor.fetchall()
      
      column_names = [desc[0] for desc in cursor.description]
      for row in results:
        print(tabulate(results,headers = column_names,tablefmt='grid'))
        return results
  except Exception as e:
    print(f'Error while view transaction:{e}')
  finally:
    if connection:
      connection.close()      