# Python CRUD Application for Pharmacy Clinic

A comprehensive Python application for managing Product Stock data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

In 2023/2024, the Ministry of Health in Indonesia will implement a new regulation that requires all clinic or similar health facilites to integrate their internal systems with Ministry of Health's centralized system. The system currently used by the clinic, which still uses Microsoft Excel, cannot be easily integrated with the centralized system. Therefore, pharmaceutical clinics need a warehousing program that can be integrated with the central system owned by the Ministry of Health, where python can be an alternative used in this case. 

This project caters to the [Industry/Business Domain] industry, specifically addressing the need to manage [Data Entity] data efficiently. [Data Entity] plays a crucial role in [Explain the importance of data entity in business processes].

**Benefits:**

* Improved data accuracy and consistency
* Streamlined data management processes
* Enhanced decision-making through readily available data
* ... (List additional benefits relevant to the business)

**Target Users:**

This application is designed for Pharmacy and Business Owner within the organization to facilitate their Task and Activities related to medicine product and medicine product stocks.

## Features

* **Show Product:**
    * Display the Product IDs, Product Names, Product Stocks, Price of Products, and Supplier Names we work with.
    * User-friendly format
* **Add Product:**
    * Add new Product (it can be a medical essentials or medicine drugs) entries with essential details like
      [Product ID, Product Name, Product Stocks, Product Price, Product Supplier Name].
    * User-friendly format
* **Edit Product:**
    * Edit data such as product name and price if there is a typo when entering additional product data in the "add product" feature.
    * The product ID will not be replaced because it must be set when adding a product in the "add product" feature. 
    * User-friendly format.
    * Provide clear confirmation or error messages based on update success or failure.
* **Update Product:**
    * Modify existing Product Stocks data to reflect changes in available stocks.
    * Stock will automatically be updated when there is an inbound stocks and or outbound stocks.
    * Provide clear confirmation or error messages based on update success or failure.
* **Delete Product:**
    * This feature aims to remove products (in the form of medical essentials and/or medicine drugs) whose suppliers are no longer cooperating with pharmacies or clinics.
    * .
* **Summary Product Stocks:**
    * This feature aims to provide conclusions to business owners and pharmacists that the availability of stock that needs to be filled for a week / 7 days.
    * So that pharmacists can add stocks that are not available for use in the next week.
    * This feature can also be used as material for decision-making (sek buntu :" )

## Installation

1. **Prerequisites:**
    * Python version (specify the required version)
    * Prettytables in library

2. **Installation:**
    ```bash
    git clone https://github.com/ratihbudii/python_crudprogram_pharmacy_clinic.git
    cd <python_crudprogram_pharmacy_clinic>
    pip install -r requirements.txt  # If using a requirements.txt file
    pip install prettytable # For table in show product list and summary product stocks feature
    ```

3. **Database Setup (if applicable):**
    Follow specific instructions for configuring your database connection, aligning with the business's chosen database management system.

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new [Data Entity] record, for example, a new customer in a customer management system, providing details like name, contact information, and preferences.
    * **Read:** Search and retrieve customer information by name, ID, or other relevant criteria.
    * **Update:** Modify customer details, such as updating their address or contact details.
    * **Delete:** Remove a customer record from the system (with appropriate authorization, if applicable).

## Data Model
This project utilizes a [Data Structure] (e.g., relational database, JSON documents) to represent [Data Entity] data. The following fields are typically stored:
   * [Field 1]: (Data type) - Description of the field's purpose in the business context.
   * [Field 2]: (Data type) - Description of the field's purpose in the business context.
   * ... (List all relevant fields)

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to [your_email] or submit an issue if you encounter any problems or have suggestions for improvements.

