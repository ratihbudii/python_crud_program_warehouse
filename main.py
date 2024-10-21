# ===================================
# [Clinical Pharmacy]
# ===================================
# Developed by. [Ratih Budi Setyorini]
# JCDS - [0412]


# /************************************/

# /===== Importing Libraries =====/
from prettytable import PrettyTable # untuk bikin table di "show product" dan "summary product stocks" features

# /===== Data Model =====/
# Create your data model here
product1 = {
    "Product ID" : "Tong001",
    "Medicine Name" : "Paracetamol",
    "Stock" : 90,
    "Price" : 2300,
    "Supplier Name" : "PT. Mersifarma TM"
    }

product2 = {
    "Product ID" : "Tong002",
    "Medicine Name" : "Rhinose",
    "Stock" : 5,
    "Price" : 15000,
    "Supplier Name" : "Dexa Medica"
    }

product3 = {
    "Product ID" : "Tong003",
    "Medicine Name" : "Ibuprofen",
    "Stock" : 20,
    "Price" : 4800,
    "Supplier Name" : "PT. First Medifarma"
    }

product4 = {
    "Product ID" : "Tong004",
    "Medicine Name" : "Amoxicillin",
    "Stock" : 10,
    "Price" : 10000,
    "Supplier Name" : "Hexpharm Jaya Laboratories"
}

product5 = {
    "Product ID" : "Tong005",
    "Medicine Name" : "Omeprazole",
    "Stock" : 7,
    "Price" : 12000,
    "Supplier Name" : "PT. Medifarma"
}

list_product = [product1, product2, product3, product4, product5]

# /===== End Data Model =====/

# /===== Feature Program =====/
# Show Product and Product Stock Feature
def print_list_product():
  print("Show Product and Product Stocks")
  list_prod_table = PrettyTable(["Product ID", "Medicine Name", "Stock", "Price", "Supplier Name"])
  for product in list_product :
    list_prod_table.add_row([product["Product ID"], product["Medicine Name"], product["Stock"], product["Price"], product["Supplier Name"]])
  print(list_prod_table)

# Add Product Feature
def add_new_product():
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
  while isiterateprice == True: #  Try except digunakan utk kalo misal yg diinput bukan integer
    try:
      new_medicine_price = int(input("Enter new price: "))
      isiterateprice = False
      break
    except ValueError:
      print("Invalid input. Please enter a valid new stock in integer.")
  new_medicine_supplier_name = input("Enter new supplier name: ")
  new_product = {
    "Product ID" : new_medicine_product_id,
    "Medicine Name" : new_medicine_name,
    "Stock" : new_medicine_stock,
    "Price" : new_medicine_price,
    "Supplier Name" : new_medicine_supplier_name
  }
  list_product.append(new_product)
  print("Successfully created " + new_medicine_name)

# Edit Product Name and Product Price Feature
def edit_product():
  isfound = False
  print("Edit Product")
  search_medicine_product_id = input("Enter Product ID: ")
  search_medicine_name = input("Enter medicine name: ")
  for product in list_product:
    if product["Product ID"] == search_medicine_product_id and product["Medicine Name"] == search_medicine_name :
      print("Product is found")
      update_medicine_name = input("Enter new medicine name: ")
      update_medicine_price = input("Enter new price: ")
      update_medicine_supplier_name = input("Enter new supplier name: ")
      product.update({"Medicine Name": update_medicine_name})
      product.update({"Price": update_medicine_price})
      product.update({"Supplier Name": update_medicine_supplier_name})
      print("Successfully updated " + search_medicine_name + " into " + update_medicine_name)
      isfound = True
      break 
  if isfound == False:
    print("Product is not found")

# Update Product Stocks Feature
def update_product_stocks():
  isfound = False
  print("Update Product Stocks")
  search_medicine_product_id = input("Enter Product ID: ")
  search_medicine_name = input("Enter medicine name: ")
  for product in list_product:
    if product["Product ID"] == search_medicine_product_id and product["Medicine Name"] == search_medicine_name :
      print("Product is found")
      current_stocks = product["Stock"]
      update_stocks_confirmation = input("What do you want to do? (1. Inbound stocks or 2. Outbound stocks): ") # kalo sad flow alias kalo salah entry terus perulangan piye? -> backlog
      while update_stocks_confirmation != "1" and update_stocks_confirmation != "2":
        print("Wrong input. Try again")
        update_stocks_confirmation = input("What do you want to do? (1. Inbound stocks or 2. Outbound stocks): ")
      if update_stocks_confirmation == "1" :
        inbound_medicine_stocks = int(input("Enter inbound medicine stocks: "))
        product.update({"Stock": current_stocks + inbound_medicine_stocks})
        print("Successfully updated " + search_medicine_name + " stocks into " + str(product["Stock"]))
        isfound = True
      elif update_stocks_confirmation == "2" :
        outbound_medicine_stocks = int(input("Enter outbound medicine stocks: "))
        product.update({"Stock": current_stocks - outbound_medicine_stocks})
        print("Successfully updated " + search_medicine_name + " stocks into " + str(product["Stock"]))
        isfound = True
      else:
        print("Wrong input. Try again")
  if isfound == False:
    print("Product is not found")

    # Cari produk yang ingin di update
    # Kalau udah ketemu, tampilin menu mau nambah stok atau ngurangi stok
    # Kalau pengen nambah, tambah stok
    # Kalau pengen ngurangi, ya kurangi stok
    # Tampilin kalo udh selesai di update dgn nunjukin update nya

# Delete Product Feature -- Produk yang sudah tidak kerjasama lagi dengan apotek/klinik
def delete_product():
  isfound = False
  # index = 0
  print("Delete Product)")
  search_medicine_product_id = input("Enter Product ID: ")
  search_medicine_name = input("Enter medicine name: ")
  for product in list_product :
    if product["Product ID"] == search_medicine_product_id and product["Medicine Name"] == search_medicine_name:
      print("Product is found")
      delete_product_confirmation = input("Do you want to delete this product? (yes or not): ") # kalo sad flow alias kalo salah entry terus perulangan piye? -> backlog
      while delete_product_confirmation != "yes" and delete_product_confirmation != "not":
        print("Wrong input. Try again")
        delete_product_confirmation = input("Do you want to delete this product? (yes or not): ")
      if delete_product_confirmation == "yes":
        index = list_product.index(product)
        del list_product[index]
        isfound = True
        print("This product is deleted")
        break
      elif delete_product_confirmation == "not":
        print("Product is not deleted")
        isfound = True
        break
      else:
        print("Wrong input. Try again")
    # index = index + 1
  if isfound == False:
    print("Product is not found")

    # Cari produk yang ingin di update
    # Kalau udah ketemu, tampilin menu mau di delete dari list atau ngga
    # Kalau pengen delete, ya tinggal delete
    # Tampilin kalo udh selesai di delete, ditunjukin update (?) atau bilang aja kalo sukses di delete dr list

# Summary Product Stocks -- Selama seminggu produk apa yang stoknya kurang dari 10
def summary_product_stocks():
  print("Summary Product Stocks")
  print("Current Product and Product Stocks for a week that are less than 10 are: ")
  list_prod_table = PrettyTable(["Product ID", "Medicine Name", "Stock", "Price", "Supplier Name"])
  for product in list_product:
    if product["Stock"] < 10:
      list_prod_table.add_row([product["Product ID"], product["Medicine Name"], product["Stock"], product["Price"], product["Supplier Name"]])
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
    print("6. Summary Product Stocks ") # Selama seminggu, produk apa aja yg stock nya kurang dari 10
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
      add_new_product()
      loop = True
    elif choice == 3:
      edit_product()
      loop = True
    elif choice == 4:
      update_product_stocks()
      loop = True
    elif choice == 5:
      delete_product()
      loop = True
    elif choice == 6:
      summary_product_stocks()
      loop = True
    elif choice == 7:
      print("Thank you for visit. See you!")
      loop = False
    else :
      print("Wrong input. Try again")

input_choice()

