import time
from constants import banner, error, get_int
from users import load_users, admin_user, customer_user, load_orders
from auth import login, register
from fruit import load_fruits
from cart import load_cart_items
from orders import load_orders_for_user

load_fruits()
load_users()
load_orders()

banner('Welcome to FruitChain')
current_user = None           

while True:
    if current_user:
        banner(f'Hello, {current_user.fullname}')
    if current_user == None:
        print('Enter your option:\n1. Login\n2. Register\n3. Exit')
        option = get_int()

        if option == 1:
            current_user = login()
        elif option == 2:
            current_user = register()
        elif option == 3:
            banner("FruitChain is shutting down...")
            time.sleep(4)
            banner("Thank you!")
            break
        else:
            error("Ops! You have chosen an invalid option!")

    else:
        if current_user.is_admin():
            while True:
                print("Enter your option:\n1. Add new fruit\n2. Update fruit\n3. Manage stock\n4. Manage users\n5. Manage orders\n6. Profile\n7. Logout")
                op = get_int()
                if op in range(1,7):
                    admin_user(current_user, op)
                elif op == 7:
                    break
                else:
                    error("Ops! You have chosen an invalid option!")
    
        else:
            load_cart_items(current_user)
            load_orders_for_user(current_user)
            while True:
                print("Enter your option:\n1. See available fruits\n2. Flash-sale\n3. Cart\n4. Orders\n5. Profile\n6. Logout")    
                op = get_int()
                if op in range(1,6):
                    customer_user(current_user, op)
                elif op == 6:
                    break
                else:
                    error("Ops! You have chosen an invalid option!")
    

        current_user = None
        print("\nLogged out successfully!\n")