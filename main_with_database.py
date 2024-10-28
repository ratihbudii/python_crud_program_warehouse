# ===================================
# [Clinical Pharmacy]
# ===================================
# Developed by. [Ratih Budi Setyorini]
# JCDS - [0412]


# /************************************/

# /===== Importing Libraries =====/
import mysql.connector
import uuid
from prettytable import PrettyTable

#  /===== Connect to Database =====/
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


# /===== Feature Program =====/

# Show List Product Feature
def print_list_product():
  print("Show Product and Product Stocks")
  myCursor = conn.cursor()
  myCursor.execute("SELECT * FROM Product")
  list_product = myCursor.fetchall()
  list_prod_table = PrettyTable(['productName','productStock','productPrice','productID','supplierID'])
  for product in list_product :
    list_prod_table.add_row([product[0], product[1], product[2], product[3], product[4]])
  print(list_prod_table)
   

# Validate Supplier
def validate_supplier(conn, supplierID):
    myCursor = conn.cursor()
    myCursor.execute("SELECT * FROM Supplier WHERE supplierID = '"+ supplierID +"'") #petik 1 buat spesifik query, utk cut string supaya bisa di concat pake petik 2, concat pake + var / nilai yg mau di concat, ditutup lagi pake + terus petik 2 sama petik 1 
    supplier = myCursor.fetchall()
    return supplier

# Add Supplier 
def add_new_supplier(conn):
    print("Add New Supplier")
    new_supplier_id = input("Enter new supplier ID: ")
    new_supplier_name = input("Enter new supplier name: ")
    new_supplier_address = input("Enter new supplier address: ")

    insert_supplier_query = """
    INSERT INTO supplier (supplierID, supplierName, supplierAddress)
    VALUES (%s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(insert_supplier_query, (new_supplier_id, new_supplier_name, new_supplier_address))
    conn.commit()
    print("Successfully created new supplier:", new_supplier_name)
              
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
      print("Invalid input. Please enter a valid new price in integer.")
  new_medicine_supplier_id = input("Enter new supplier ID: ")
  supplier = validate_supplier(conn, new_medicine_supplier_id)
  if len(supplier) == 1:
      insert_query = """
      INSERT INTO Product (productID, productName, productStock, productPrice, supplierID)
      VALUES (%s, %s, %s, %s, %s)
      """ # SQL INSERT query
      cursor = conn.cursor()
      cursor.execute(insert_query, (new_medicine_product_id, new_medicine_name, new_medicine_stock, new_medicine_price, new_medicine_supplier_id))
      conn.commit()
      print("Successfully created " + new_medicine_name) # Execute the query with the new product data
  else:
      print("Supplier not found. Please add supplier first")
      add_new_supplier(conn)

# Edit Product Name and Product Price Feature
def edit_product(conn):
  isfound = False
  print("Edit Product")
  search_medicine_product_id = input("Enter Product ID: ")
  search_medicine_name = input("Enter medicine name: ")
  # SQL SELECT query to find the product
  select_query = """
  SELECT * FROM Product
  WHERE productID = %s AND productName = %s
  """
  # SQL UPDATE query to update the product
  update_query = """
  UPDATE Product
  SET productName = %s, productPrice = %s
  WHERE productID = %s AND productName = %s
  """

  cursor = conn.cursor()
  cursor.execute(select_query, (search_medicine_product_id, search_medicine_name))
  result = cursor.fetchone()
  if result :
    isfound = True
    update_medicine_name = input("Enter new medicine name: ")
    update_medicine_price = input("Enter new price: ")

    cursor.execute(update_query, (update_medicine_name, update_medicine_price, search_medicine_product_id, search_medicine_name))
    conn.commit()
    print("Successfully updated " + search_medicine_name + " into " + update_medicine_name)
  else:
     print("Product is not found")


# Update Product Stocks Feature 
def update_product_stocks(conn):
  isfound = False
  print("Update Product Stocks")
  search_medicine_product_id = input("Enter Product ID: ")
  # SQL SELECT query to find the product
  select_product_query = """
  SELECT * FROM Product
  WHERE productID = %s
  """
  cursor = conn.cursor()
  cursor.execute(select_product_query, (search_medicine_product_id,))
  result = cursor.fetchone()
  cursor.close()
  if result:
    isfound = True
    productID = result[3]
    print("Product is found")
    update_stocks_confirmation = input("What do you want to do? (1. Inbound stocks or 2. Outbound stocks): ")
    while update_stocks_confirmation not in ["1", "2"]:
      print("Wrong input. Try again")
      update_stocks_confirmation = input("What do you want to do? (1. Inbound stocks or 2. Outbound stocks): ")
    if update_stocks_confirmation == "1":
      inbound_medicine_stocks = int(input("Enter inbound medicine stocks: "))
      stock_id = str(uuid.uuid4())
      insert_stock_query = """
      INSERT INTO Stock (amount, stockID, productID)
      VALUES (%s, %s, %s)
      """
      cursor = conn.cursor()
      cursor.execute(insert_stock_query, (inbound_medicine_stocks, stock_id, productID))
      conn.commit()
      print("Successfully added " + search_medicine_product_id + " inbound stocks ")
    elif update_stocks_confirmation == "2":
      outbound_medicine_stocks = int(input("Enter outbound medicine stocks: "))
      stock_id = str(uuid.uuid4())
      insert_stock_query = """
      INSERT INTO Stock (amount, stockID, productID)
      VALUES (%s, %s, %s)
      """
      cursor = conn.cursor()
      cursor.execute(insert_stock_query, (outbound_medicine_stocks, stock_id, productID))
      conn.commit()
      print("Successfully added " + search_medicine_product_id + " outbound stocks ")
  else :
    print("Product not found.")


# Delete Product Feature
def delete_product(conn):
  isfound = False
  print("Delete Product")
  search_medicine_product_id = input("Enter Product ID: ")
  search_medicine_name = input("Enter medicine name: ")

  # SQL SELECT query to find the product
  select_query = """
  SELECT * FROM Product
  WHERE productID = %s AND productName = %s
  """

  # SQL DELETE query to delete the stock
  delete_stock_query = """
  DELETE FROM Stock
  WHERE productID = %s
  """

  # SQL DELETE query to delete the product
  delete_query = """
  DELETE FROM Product
  WHERE productID = %s
  """

  cursor = conn.cursor()
  cursor.execute(select_query, (search_medicine_product_id, search_medicine_name))
  result = cursor.fetchone()

  if result:
    isfound = True
    delete_product_confirmation = input("Do you want to delete this product? (yes or not): ")
    while delete_product_confirmation not in ["yes", "not"]:
      print("Wrong input. Try again")
      delete_product_confirmation = input("Do you want to delete this product? (yes or not): ")
    if delete_product_confirmation == "yes":
      cursor.execute(delete_stock_query,(search_medicine_product_id,))
      conn.commit()
      cursor.execute(delete_query, (search_medicine_product_id,))
      conn.commit()
      print("This product is deleted.")
    elif delete_product_confirmation == "not":
      print("This product is not deleted.")


# Summary Product Stocks
def summary_product_stocks(conn):
  print("Summary Product Stocks")
  print("Top 3 Current Product and Product Stocks for a week are: ")
  # SQL SUM, JOIN, Top 3 query to sum the product stocks
  top_three_query = """
  SELECT SUM(amount) as amount_stock, s.productID, p.productName
  FROM stock as s
  JOIN product as p
  ON s.productID = p.productID
  GROUP BY s.productID, p.productName
  ORDER BY amount_stock desc
  LIMIT 3;
  """
  cursor = conn.cursor()
  cursor.execute(top_three_query)
  result = cursor.fetchall()

  list_prod_table = PrettyTable(['amount_stocks', 'productID', 'productName'])
  for product in result :
    list_prod_table.add_row([product[0], product[1], product[2]])
  print(list_prod_table)


# /===== End of Feature Program =====/

# /===== Start to main program =====/

def print_menu():
    print(40 * "-", "Farmacy Clinic TongFunk", 40 * "-")
    print("1. Show Product Stocks ")
    print("2. Add Product ")
    print("3. Edit Product ")
    print("4. Update Product Stocks ")
    print("5. Delete Product ")
    print("6. Summary Product Stocks ") # Top 3 Current Product and Product Stocks for a week
    print("7. Exit from the menu ")
    print(73 * "-")

def input_choice ():
  loop = True

  while loop:
    print_menu()
    choice = int(input("Enter your choice [1-7]: "))
    if choice == 1:
      print_list_product()
      loop = True
    elif choice == 2:
      add_new_product_to_db(conn)
      loop = True
    elif choice == 3:
      edit_product(conn)
      loop = True
    elif choice == 4:
      update_product_stocks(conn)
      loop = True
    elif choice == 5:
      delete_product(conn)
      loop = True
    elif choice == 6:
      summary_product_stocks(conn)
      loop = True
    elif choice == 7:
      print("Thank you for visit. See you!")
      loop = False
    else :
      print("Wrong input. Try again")

# Show pharmacy data
conn = create_connection("pharmacy_clinic")
input_choice()