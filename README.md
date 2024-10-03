**Restaurant Management Web App**
=================================

This is a simple Restaurant Management web application built with Python, Flask, and SQLAlchemy. The system handles customer orders, menu items, categories, and restaurants. It supports creating orders, managing menu items, and associating them with restaurants and categories.

**Table of Contents**
---------------------

*   [Project Overview](#project-overview)
*   [Technologies Used](#technologies-used)
*   [Features](#features)
*   [Database Schema](#database-schema)
*   [Setup and Installation](#setup-and-installation)
*   [Running the Application](#running-the-application)
*   [API Endpoints](#api-endpoints)
*   [Contributing](#contributing)
*   [License](#license)

**Project Overview**
--------------------

This project is a full-stack web application that includes:

*   **Backend**: Built with Flask, it handles all the data management and business logic.
*   **Database**: SQLAlchemy and Flask-Migrate manage the relational database, which stores restaurant information, menu items, customers, orders, and categories.
*   **Frontend**: A basic HTML/CSS/JavaScript frontend to interact with the system, which you can enhance as needed.

**Technologies Used**
---------------------

*   **Backend**: Flask, Python, SQLAlchemy, Flask-Migrate
*   **Frontend**: HTML, CSS, JavaScript (optional)
*   **Database**: SQLite (by default), can be configured for other databases (PostgreSQL, MySQL, etc.)
*   **Deployment**: Flask development server

**Features**
------------

*   **Restaurant Management**: Add restaurants and manage their details (name, address, phone).
*   **Menu Items**: Define menu items and assign them to restaurants and categories.
*   **Category Management**: Classify menu items by categories.
*   **Order Management**: Customers can place orders, and each order can include multiple menu items.
*   **Customer Management**: Store customer details and link them to their orders.
*   **Database Migrations**: Use Flask-Migrate to manage database schema changes.

**Database Schema**
-------------------

Below is an overview of the database structure used in this project:

*   **Restaurant**: Stores restaurant details.
*   **MenuItem**: Stores menu items with a relationship to a restaurant and a category.
*   **Category**: Defines categories for menu items (e.g., Drinks, Main Course).
*   **Customer**: Stores customer details.
*   **Order**: Represents an order placed by a customer.
*   **OrderItem**: Stores the individual menu items within an order.

The database schema can be visualized as follows:

### **ER Diagram** (Paste this into [dbdiagram.io](https://dbdiagram.io) to generate the diagram):

```plaintext
Table Restaurant {
    id int [pk, increment]
    name varchar(100)
    address varchar(200)
    phone varchar(15)
}

Table MenuItem {
    id int [pk, increment]
    name varchar(100)
    price float
    description varchar(200)
    restaurant_id int [ref: > Restaurant.id]
    category_id int [ref: > Category.id]
}

Table Category {
    id int [pk, increment]
    name varchar(100)
}

Table Customer {
    id int [pk, increment]
    first_name varchar(50)
    last_name varchar(50)
    email varchar(120) [unique]
    phone varchar(15)
}

Table Order {
    id int [pk, increment]
    order_date datetime
    total_amount float
    customer_id int [ref: > Customer.id]
}

Table OrderItem {
    id int [pk, increment]
    quantity int
    menu_item_id int [ref: > MenuItem.id]
    order_id int [ref: > Order.id]
}

Ref: MenuItem.restaurant_id > Restaurant.id
Ref: MenuItem.category_id > Category.id
Ref: Order.customer_id > Customer.id
Ref: OrderItem.menu_item_id > MenuItem.id
Ref: OrderItem.order_id > Order.id
```

**Setup and Installation**
--------------------------

### **Prerequisites**

*   Python 3.x
*   Virtual environment tool (`venv` or `virtualenv`)
*   SQLite (installed by default with Python)

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/rushionsdomain/Flask-Begins-.git
cd Flask-Begins-
```

### **Step 2: Create and Activate a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **Step 3: Install the Required Packages**

```bash
pip install -r requirements.txt
```

### **Step 4: Set Up the Database**

1.  Initialize the database migration repository:
    
    ```bash
    flask db init
    ```
    
2.  Generate the initial migration:
    
    ```bash
    flask db migrate -m "Initial migration"
    ```
    
3.  Apply the migration to the database:
    
    ```bash
    flask db upgrade
    ```
    

### **Step 5: Run the Application**

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000`.

**API Endpoints**
-----------------

### **Restaurant Endpoints**

*   `GET /restaurants`: Fetch all restaurants.
*   `POST /restaurants`: Create a new restaurant.
*   `GET /restaurants/<id>`: Get details of a specific restaurant.
*   `PUT /restaurants/<id>`: Update restaurant information.
*   `DELETE /restaurants/<id>`: Delete a restaurant.

### **Menu Item Endpoints**

*   `GET /menu_items`: Fetch all menu items.
*   `POST /menu_items`: Create a new menu item.
*   `GET /menu_items/<id>`: Get details of a specific menu item.
*   `PUT /menu_items/<id>`: Update menu item information.
*   `DELETE /menu_items/<id>`: Delete a menu item.

### **Category Endpoints**

*   `GET /categories`: Fetch all categories.
*   `POST /categories`: Create a new category.

### **Order Endpoints**

*   `POST /orders`: Create a new order.
*   `GET /orders`: Get all orders.

**Contributing**
----------------

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature-branch`).
3.  Commit your changes (`git commit -m 'Add a new feature'`).
4.  Push to the branch (`git push origin feature-branch`).
5.  Open a pull request.

**License**
-----------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
