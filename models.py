from app import db

# Model for Restaurant
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    # Relationship with MenuItem (a restaurant can have many menu items)
    menu_items = db.relationship('MenuItem', backref='restaurant', lazy=True)

    def __repr__(self):
        return f'<Restaurant {self.name}>'


# Model for MenuItem
class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))

    # Foreign key linking to Restaurant
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    # Relationship with Category (many-to-one)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f'<MenuItem {self.name}>'


# Model for Category
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationship with MenuItem (a category can have many menu items)
    menu_items = db.relationship('MenuItem', backref='category', lazy=True)

    def __repr__(self):
        return f'<Category {self.name}>'


# Model for Customer
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    # Relationship with Order (a customer can place many orders)
    orders = db.relationship('Order', backref='customer', lazy=True)

    def __repr__(self):
        return f'<Customer {self.first_name} {self.last_name}>'


# Model for Order
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

    # Foreign key linking to Customer
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    # Relationship with OrderItem (an order can have many items)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

    def __repr__(self):
        return f'<Order {self.id} for Customer {self.customer_id}>'


# Model for OrderItem
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    # Foreign key linking to MenuItem
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)

    # Foreign key linking to Order
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)

    def __repr__(self):
        return f'<OrderItem {self.id} - {self.quantity}x {self.menu_item_id}>'
