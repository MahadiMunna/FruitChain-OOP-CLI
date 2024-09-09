from constants import generate_hash, error, success, get_int
from fruit import Fruit, add_fruit, view_fruits, update_fruit, manage_stock, user_fruits_view, flash_sale
from cart import add_to_cart, view_cart
from orders import view_orders, manage_orders

class User(object):
    
    user_list = []
    username_list = []
    def __init__(self, user_name, first_name, last_name, email, gender, password):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.__password = generate_hash(password)
        self.__admin = False
        self.cart = []
        self.orders = []
        User.username_list.append(self.user_name)
        User.user_list.append(self)

    
    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'    

    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = password
    
    def make_admin(self):
        self.__admin = True

    def remove_admin(self):
        self.__admin = False
    
    def is_admin(self):
        return self.__admin
    
    def get_total_amount(self):
        total = 0
        for item in self.cart:
            total+=item.total_price
        return total
    
def admin_user(current_user, op):
    if op == 1:
        add_fruit()
    elif op == 2:
        view_fruits()
        update_fruit()
    elif op == 3:
        view_fruits()
        manage_stock()
    elif op == 4:
        view_users()
        manage_users()
    elif op == 5:
        manage_orders()
    elif op == 6:
        profile(current_user)

def customer_user(current_user, op):
    if op == 1:
        user_fruits_view()
        add_to_cart(current_user)
    elif op == 2:
        flash_sale()
        add_to_cart(current_user)
    elif op == 3:
        view_cart(current_user)
    elif op == 4:
        view_orders(current_user)
    elif op == 5:
        profile(current_user)


def profile(current_user):
    print("\nWelcome to profile, " + current_user.fullname)
    while True:
        print("\nChoose your option from below: \n1. Update profile\n2. Change password\n0. Back")
        option = get_int()

        if option == 1:
            print(f"\nYour current profile information-\nName: {current_user.fullname}\nEmail: {current_user.email}\nGender: {current_user.gender}\n")
            current_user.first_name = input("Enter your first name: ")
            current_user.last_name = input("Enter your last name: ")
            current_user.email = input("Enter your email: ")
            current_user.gender = input("Enter your gender(Male/Female): ")
            success("Profile updated successfully!")
                
        elif option == 2:
            current_pass = input("Enter your current password: ")
            password = generate_hash(current_pass)
            if current_user.get_password() == password:
                new_pass = input("Enter your new password: ")
                re_pass = input("Re-type your new password: ")
                if new_pass == re_pass:
                    password = generate_hash(new_pass)
                    current_user.set_password(password)
                    success("Password changed successfully!")
                    
                else:
                    error("Passwords do not match. Try again.")
                    
            else:
                error("Passwords do not match. Try again.")
                
        elif option == 0:
            print()
            break
        else:
            error("Ops! You have chosen an invalid option!")
            

def view_users():
    for index, user in enumerate(User.user_list):
        print('='*7 + f' User No: {index+1} ' + '='*7)
        print(f'Name: {user.fullname}', end=" ")
        if user.is_admin() == True:
            print('(Admin)', end=" ")
        print(f'\nEmail: {user.email}')
        print('='*len('='*7 + f' User No: {index+1} ' + '='*7)+'\n')


def manage_users():
    print("\nChoose your option from below: \n1. Add new user\n2. Remove user\n3. Manage admin\n0. Back ")
    option = get_int()

    if option == 1:
        user_name = input("Username: ")
        if user_name in User.username_list:
            error("Username already taken. Try again.")
            return
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        gender = input("Gender(Male/Female): ")
        password = input("Password: ")
        re_pass = input("Re-type password: ")
        if password != re_pass:
            error("Passwords do not match. Try again.")
            
        else:
            success("New user account created successfully!")
            
            User(user_name, first_name, last_name, email, gender, password)
    elif option == 2:
        print("Enter user no to remove:", end=" ")
        no = get_int()
        if no not in range(1,len(User.user_list)+1):
            error("Invalid user no. Try again.")    
            return
        user = User.user_list[no-1]
        User.user_list.remove(user)
        success(f"{user.fullname} removed successfully.")
        
    elif option == 3:
        print("\nChoose your option from below: \n1. Make new admin\n2. Remove from admin\n0. Back ")
        option = get_int()
        if option == 0:
            return
        elif option == 1:
            print("Enter user no to make admin:",end=" ")
            no = get_int()
            if no not in range(1,len(User.user_list)+1):
                error("Invalid user no. Try again.")
                return
            user = User.user_list[no-1]
            if user.is_admin():
                error("This user is already admin!")
                return
            user.make_admin()
            success(f"{user.fullname} made admin successfully.")
            
        elif option == 2:
            print("Enter user no to remove from admin:", end=" ")
            no = get_int()
            if no not in range(1,len(User.user_list)+1):
                error("Invalid user no. Try again.")
                return
            user = User.user_list[no-1]
            if user.is_admin():
                user.remove_admin()
                success(f"{user.fullname} removed from admin")
            else:
                error("This user is not admin!")
        else:
            error("Ops! You have chosen an invalid option!")
    elif option == 0:
        return
    else:
        error("Ops! You have chosen an invalid option!")
            
