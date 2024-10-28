/* Create the database */
CREATE DATABASE IF NOT EXISTS pharmacy_clinic;

/* Switch to the pharmacy_clinic database */
USE pharmacy_clinic;

/* Drop existing tables */
DROP TABLES IF EXISTS Supplier;
DROP TABLES IF EXISTS Product;
DROP TABLES IF EXISTS Stocks;

/* Create the tables */
CREATE TABLE Supplier
(
  supplierName VARCHAR(255) NOT NULL,
  supplierAddress VARCHAR(255) NOT NULL,
  supplierID VARCHAR(10) NOT NULL,
  PRIMARY KEY (supplierID)
);

CREATE TABLE Product
(
  productName VARCHAR(255) NOT NULL,
  productStock INT NOT NULL,
  productPrice INT NOT NULL,
  productID VARCHAR(10) NOT NULL,
  supplierID VARCHAR(10) NOT NULL,
  PRIMARY KEY (productID),
  FOREIGN KEY (supplierID) REFERENCES Supplier(supplierID)
);

CREATE TABLE Stock
(
  amount INT NOT NULL,
  stockID VARCHAR(10) NOT NULL,
  productID VARCHAR(10) NOT NULL,
  PRIMARY KEY (stockID),
  FOREIGN KEY (productID) REFERENCES Product(productID)
);

/* Insert Data */
insert into Supplier(supplierID,supplierName,supplierAddress) values
('S001', 'PT. Mersifarma TM', 'Jalan Raya Pelabuhan Km. 18 Cikembar Sukabumi - Jawa Barat'),
('S002','Dexa Medica','Titan Center, Lantai 3, Jalan Boulevard Bintaro, Blok B7/B1 No. 5, Bintaro Jaya, Sektor 7, Tangerang'),
('S003','PT First Medipharma','Raya Sumorame no 41, Candi, Sidoarjo'),
('S004','PT. Hexpharm Jaya Laboratories','Jl. Berbek Industri VII No.6-10, Ngeni, Kepuhkiriman, Kec. Waru, Kabupaten Sidoarjo'),
('S005','PT. Mediafarma Laboratories','Jl. Raya Jakarta-Bogor No.KM. 33, Curug, Kec. Cimanggis, Kota Depok');

insert into Product(productID,productName,productStock,productPrice,supplierID) values
('Tong001','Paracetamol',90,2300,'S001'),
('Tong002','Rhinose',5,10000,'S002'),
('Tong003','Ibuprofen',20,4800,'S003'),
('Tong004','Amoxicilin',10,10000,'S004'),
('Tong005','Omeprazole',7,12000,'S005');

insert into Stock(stockID,productID,amount) values
('ST001','Tong001',10),
('ST002','Tong001',30),
('ST003','Tong002',20),
('ST004','Tong001',-10),
('ST005','Tong006',20),
('ST006','Tong005',10),
('ST007','Tong003',20);
