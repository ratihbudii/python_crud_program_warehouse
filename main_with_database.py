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

# Show List Product Feature
def print_list_product():
   print("Show Product and Product Stocks")
   list_prod_table = PrettyTable([a, b, c, d, e])
   for product in data :
    list_prod_table.add_row([product[0], product[1], product[2], product[3], product[4]])
    print(product)
   print(list_prod_table)
   

print_list_product()

# Validate Supplier
def validate_supplier(conn, supplierId):
    myCursor = conn.cursor()
    myCursor.execute("SELECT * FROM Supplier WHERE supplierId = '"+ supplierId +"'") #petik 1 buat spesifik query, utk cut string supaya bisa di concat pake petik 2, concat pake + var / nilai yg mau di concat, ditutup lagi pake + terus petik 2 sama petik 1 
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
      print("Invalid input. Please enter a valid new stock in integer.")
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

add_new_product_to_db(conn)

# Edit Product Name and Product Price Feature
def edit_product(conn):
  isfound = False
  print("Edit Product")
  search_medicine_product_id = input("Enter Product ID: ")
  search_medicine_name = input("Enter medicine name: ")
  # SQL SELECT query to find the product
  select_query = """
  SELECT * FROM Product
  WHERE productId = %s AND productName = %s
  """
  # SQL UPDATE query to update the product
  update_query = """
  UPDATE Product
  SET productName = %s, productPrice = %s
  WHERE productId = %s AND productName = %s
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

edit_product(conn)

# Update Product Stocks Feature 
def update_product_stocks(conn):
  isiteratestock = True
  isiterateprice = True
  print("Update Product Stocks")
  search_medicine_product_id = input("Enter Product ID: ")
  # SQL SELECT query to find the product
  select_product_query = """
  SELECT * FROM Stock
  WHERE productId = %s
  """
  cursor = conn.cursor()
  cursor.execute(select_product_query, (search_medicine_product_id))
  result = cursor.fetchone()
  if result:
    isfound = True
    productId = result[2]
    print("Product is found")
    current_stocks = result[0]  # Assuming amount is at index 0
    update_stocks_confirmation = input("What do you want to do? (1. Inbound stocks or 2. Outbound stocks): ")
    while update_stocks_confirmation not in ["1", "2"]:
      print("Wrong input. Try again")
      update_stocks_confirmation = input("What do you want to do? (1. Inbound stocks or 2. Outbound stocks): ")
      if update_stocks_confirmation == "1":
        inbound_medicine_stocks = int(input("Enter inbound medicine stocks: "))
        new_stock = current_stocks + inbound_medicine_stocks
        update_stock_query = """
        UPDATE Stock
        SET amount = %s
        WHERE productId = %s
        """
        cursor.execute(update_stock_query, (new_stock, productId))
        conn.commit()
        print("Successfully updated " + search_medicine_name + " stocks into " + str(new_stock))


  while isiteratestock == True:
    try:
      new_medicine_stock = int(input("Enter new stock: "))
      isiteratestock = False
      break
    except ValueError:
      print("Invalid input. Please enter a valid new stock in integer.")
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

add_new_product_to_db(conn)









def update_product_stocks(conn):
  isfound = False
  print("Update Product Stocks")
  search_medicine_product_id = input("Enter Product ID: ")
  search_medicine_name = input("Enter medicine name: ")

  # SQL SELECT query to find the product
  select_product_query = """
  SELECT * FROM Product
  WHERE productId = %s AND productName = %s
  """

  cursor = conn.cursor()
  cursor.execute(select_product_query, (search_medicine_product_id, search_medicine_name))
  result = cursor.fetchone()

  if result:
    isfound = True
    productId = result[3]
    # SQL SELECT query to get the current amount from the Stock table
    select_stock_query = """
    SELECT amount 
    FROM Stock 
    WHERE productId = %s
    """
    cursor.execute(select_stock_query, (productId))
    stock_result = cursor.fetchone()
    if stock_result:
      current_stocks = stock_result[0]  # Assuming amount is at index 0
      update_stocks_confirmation = input("What do you want to do? (1. Inbound stocks or 2. Outbound stocks): ")
      while update_stocks_confirmation not in ["1", "2"]:
        print("Wrong input. Try again")
        update_stocks_confirmation = input("What do you want to do? (1. Inbound stocks or 2. Outbound stocks): ")
        if update_stocks_confirmation == "1":
          inbound_medicine_stocks = int(input("Enter inbound medicine stocks: "))
          new_stock = current_stocks + inbound_medicine_stocks
          update_stock_query = """
          UPDATE Stock
          SET amount = %s
          WHERE productId = %s
          """
          cursor.execute(update_stock_query, (new_stock, productId))
          conn.commit()
          print("Successfully updated " + search_medicine_name + " stocks into " + str(new_stock))
        elif update_stocks_confirmation == "2":
          outbound_medicine_stocks = int(input("Enter outbound medicine stocks: "))
          new_stock = current_stocks - outbound_medicine_stocks
          update_stock_query = """
          UPDATE Stock
          SET amount = %s
          WHERE productId = %s
          """
          cursor.execute(update_stock_query, (new_stock, productId))
          conn.commit()
          print("Successfully updated " + search_medicine_name + " stocks into " + str(new_stock))
    else:
      print("Stock record not found for the product.")
  else:
     print("Product not found.")

update_product_stocks(conn)




