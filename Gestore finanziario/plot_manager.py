from matplotlib import pyplot as plt
from db_manager import get_connection

def retrieve_data ():
  try:
    connection = get_connection()
    if connection:
      cursor = connection.cursor(dictionary=True)
      query = '''select 
    DATE(date) as day, 
    sum(case
            when transaction_type = 'income' then amount
            when transaction_type = 'expense' then -amount
            else 0 
        end) as total
from transaction
group by DATE(date)
order by day;
'''
      cursor.execute(query)
      results = cursor.fetchall()
      saldo_details = []
      saldo = 0 
      for row in results:
        saldo += row['total']
        saldo_details.append((row['day'],saldo))
      return saldo_details
  except Exception as e:
     print(f'Error while adding transaction:{e}')
     return []
  finally:
    if connection:
      connection.close() 
      



def plot_data():
  details = retrieve_data()
  if not details:
    print('No data found')
    return
  
  day, amount = zip(*details)
  plt.figure(figsize=(10, 6))
  plt.plot(day, amount, marker='o', color='skyblue', linestyle='-')
  plt.title('Trend amount', fontsize=16)
  plt.xlabel('Day', fontsize=14)
  plt.ylabel('Total amount (€)', fontsize=14)
  plt.xticks(rotation=45)
  plt.tight_layout()

  plt.show()