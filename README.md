# Aditya-Electronics
## Aditya Electronics: Online Shop Management Software

**Description:**

Aditya Electronics is a Python and MySQL-based software designed to manage and maintain an electronics shop. It allows you to record information on workers, customers, and products, streamlining shop operations.

**Tech Stack:**

* Python
* MySQL
* Git (Version Control)

**Pre-requisites:**

* Python (Latest Version)
* MySQL Server Installed and configured

**Before You Begin:**

1. Read about each script provided before cloning and running the project.
2. Ensure you have the latest versions of Python and MySQL installed on your system.


**Files Information:**

1. **database_creation.py:** This script creates the initial database for the shop. Run this script first.
2. **table_creation.py:** This script creates tables for employees and customers within the database. Run this script after `database_creation.py`.
3. **products.py:** This script creates tables for products and adds some basic product information. Run this script after `table_creation.py`.
4. **home_page.py:** This is the main user interface. It displays options and redirects you to specific functionalities based on your choice.
    * **buy.py:** Used by users to purchase products.
    * **insideshop.py:** Used to register and deregister as a user or employee. Additionally, you can check stock levels through this script.

**User Interfaces:**

* **ADMIN:** Full access for managing the shop. Controls include checking and updating stock, adding/removing employees and customers, adding products, and purchasing products. The default admin password is: `12345` (**Please change this immediately!**)
* **EMPLOYEES:** Authorized employees can check and update stock levels, and purchase products.
* **CUSTOMER/USER:**  Users can only check stock levels and purchase products. Each user has a unique ID and password they create during registration.


**Important Note:**

The provided code uses "123456" as the password for the MySQL server. **Please change this to a secure password before running the application.**

