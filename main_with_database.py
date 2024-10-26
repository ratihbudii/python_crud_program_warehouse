import mysql.connector

def create_connection(db:str):
    """Connect to MySql Database
    Args:
        db (str): Database name

    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ratihcantik42!",
            database=db
        )
        print("Connection success!")

        return conn
    
    except Exception as e:
        print(f"Error connecting to database: {e}")


def execute_query(conn:object, query:str):
    # 2. Create cursor - access to database
    myCursor = conn.cursor()
    # 3. Execute SQL query
    myCursor.execute(query)
    # 4. Fetch data
    return myCursor.fetchall(), myCursor.column_names # ngambil nama nama kolom dalam tabelnya (column_names)

# Show pharmacy data
conn = create_connection("pharmacy_clinic")
query = "SELECT * FROM Product"
data, column_names = execute_query(conn, query)

print(column_names)
print(data)
print(data[0][3])

a = column_names[0]
b = column_names[1]
c = column_names[2]
d = column_names[3]
e = column_names[4]


from prettytable import PrettyTable

def print_list_product():
   print("Show Product and Product Stocks")
   list_prod_table = PrettyTable([a, b, c, d, e])
   for product in data :
    list_prod_table.add_row([product[0], product[1], product[2], product[3], product[4]])
    print(product)
   print(list_prod_table)
   

print_list_product()

# Add Product Feature
def add_new_product_to_db(conn):
  isiteratestock = True
  isiterateprice = True
  print("Add Product")
  new_medicine_product_id = input("Enter new product ID: ")
  new_medicine_name = input("Enter new medicine name: ")
  while isiteratestock == True:
    try:
      new_medicine_stock = int(input("Enter new stock: "))
      isiteratestock = False
      break
    except ValueError:
      print("Invalid input. Please enter a valid new stock in integer.")
  while isiterateprice == True:
    try:
      new_medicine_price = int(input("Enter new price: "))
      isiterateprice = False
      break
    except ValueError:
      print("Invalid input. Please enter a valid new stock in integer.")
  new_medicine_supplier_name = input("Enter new supplier name: ")
  insert_query = """
  INSERT INTO Product (product_id, medicine_name, stock, price, supplier_name)
  VALUES (%s, %s, %s, %s, %s)
  """ # SQL INSERT query
  cursor = conn.cursor()
  cursor.execute(insert_query, (new_medicine_product_id, new_medicine_name, new_medicine_stock, new_medicine_price, new_medicine_supplier_name))
  conn.commit()
  print("Successfully created " + new_medicine_name) # Execute the query with the new product data

add_new_product_to_db(conn)

