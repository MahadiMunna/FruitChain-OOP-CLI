import sqlite3

conn = sqlite3.connect('fruitchain.sqlite')

cursor = conn.cursor()

# users table

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               user_name TEXT,
               first_name TEXT,
               last_name TEXT,
               email TEXT,
               gender TEXT,
               password TEXT,
               admin BOOL
               )""")

def create_user(user):
    with conn:
        cursor.execute("INSERT INTO users VALUES(:user_name, :first_name, :last_name, :email, :gender, :password, :admin)",{"user_name":user.user_name, "first_name":user.first_name, "last_name":user.last_name, "email":user.email, "gender":user.gender, "password":user.get_password(), "admin":user.is_admin()})

def update_user(user, first_name, last_name, email, gender):
    with conn:
        cursor.execute("UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, gender = :gender WHERE user_name = :user",{"first_name":first_name, "last_name":last_name, "email":email, "gender":gender, "user":user} )

def update_password(user):
    with conn:
        cursor.execute("UPDATE users SET password = :password WHERE user_name = :user", {"password":user.get_password(), "user":user.user_name})

def delete_user(user):
    with conn:
        cursor.execute("DELETE FROM users WHERE user_name = :user", {"user":user})

def make_admin_user(user):
    with conn:
        cursor.execute("UPDATE users SET admin = 1 WHERE user_name = :user", {"user":user.user_name})

def remove_admin_user(user):
    with conn:
        cursor.execute("UPDATE users SET admin = 0 WHERE user_name = :user", {"user":user.user_name})

cursor.execute("""CREATE TABLE IF NOT EXISTS fruits(
               fruit_name TEXT,
               price REAL,
               unit TEXT,
               origin TEXT,
               discount REAL,
               supply_date TEXT,
               expiry_date TEXT,
               stock_out BOOL
               )""")

# fruits table

def create_fruit(fruit):
    with conn:
        cursor.execute("INSERT INTO fruits VALUES(:fruit_name, :price, :unit, :origin, :discount, :supply_date, :expiry_date, :stock_out)", {"fruit_name":fruit.fruit_name, "price":fruit.price, "unit":fruit.unit, "origin":fruit.origin, "discount":fruit.discount, "supply_date":fruit.supply_date, "expiry_date":fruit.expiry_date, "stock_out":fruit.stock_out})

def update_fruit_db(fruit):
    with conn:
        cursor.execute("UPDATE fruits SET price = :price, unit = :unit, origin = :origin, discount = :discount, supply_date = :supply_date, expiry_date = :expiry_date WHERE fruit_name = :fruit_name", {"price":fruit.price, "unit":fruit.unit, "origin":fruit.origin, "discount":fruit.discount, "supply_date":fruit.supply_date, "expiry_date":fruit.expiry_date, "fruit_name":fruit.fruit_name})

def make_stock_out_db(fruit):
    with conn:
        cursor.execute("UPDATE fruits SET stock_out = 1 WHERE fruit_name = :fruit_name", {"fruit_name":fruit.fruit_name})

def make_stock_in_db(fruit):
    with conn:
        cursor.execute("UPDATE fruits SET stock_out = 0 WHERE fruit_name = :fruit_name", {"fruit_name":fruit.fruit_name})

# Cart table

cursor.execute("""CREATE TABLE IF NOT EXISTS cart(
               item TEXT,
               quantity INTEGER,
               total_price REAL,
               user TEXT,
               FOREIGN KEY (item) REFERENCES fruits(fruit_name),
               FOREIGN KEY (user) REFERENCES users(user_name)
               )""")

def add_to_cart_db(user, cart):
    with conn:
        cursor.execute("INSERT INTO cart VALUES(:item, :quantity, :total_price, :user)", {"item": cart.item.fruit_name, "quantity":cart.quantity, "total_price":cart.total_price, "user": user.user_name})

def remove_from_cart_db(user, cart):
    with conn:
        cursor.execute("DELETE FROM cart WHERE item = :item AND user = :user", {"item": cart.item.fruit_name, "user": user.user_name})

def update_cart_db(user, cart):
    with conn:
        cursor.execute("UPDATE cart SET quantity = :quantity, total_price = :total_price WHERE item = :item AND user = :user", {"quantity":cart.quantity, "total_price":cart.total_price, "item": cart.item.fruit_name, "user": user.user_name})

cursor.execute("""CREATE TABLE IF NOT EXISTS billing_address(
               village TEXT,
               post TEXT,
               police_station TEXT,
               district TEXT,
               phone TEXT,
               user TEXT,
               FOREIGN KEY (user) REFERENCES users(user_name)
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
               user TEXT,
               billing_address TEXT,
               items TEXT,
               total_amount REAL,
               payment_method TEXT,
               payment_status TEXT,
               order_status TEXT,
               timestamp TEXT,
               order_id TEXT,
               FOREIGN KEY(user) REFERENCES users(user_name),
               FOREIGN KEY(billing_address) REFERENCES billing_address(village),
               FOREIGN KEY(items) REFERENCES cart(item)
               )""")

conn.commit()




