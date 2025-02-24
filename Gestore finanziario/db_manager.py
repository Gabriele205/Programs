from config import db_config
import mysql.connector 

def test_connection():
  try:
    conn= mysql.connector.connect(**db_config)
    if conn.is_connected():
      print('connection to database established!')
    conn.close()
  except mysql.connector.Error as err:
    print(f'Error:{err}')
      
def get_connection():
  try:
    conn = mysql.connector.connect(**db_config)
    print('Connection to database established')
    return conn 
  except mysql.connector.Error as err:
    print(f'Error:{err}')
    return None 
   
