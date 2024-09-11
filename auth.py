from users import User
from constants import generate_hash, error, success
from db import conn,cursor,create_user


def username_validator(username):
    if username in User.username_list:
        return False
    else:
        return True
    
def login():
    username = input("Enter your username: ")
    input_pass = input("Enter your password: ")
    password = generate_hash(input_pass)
    with conn:
        cursor.execute("SELECT * FROM users WHERE user_name = :user_name AND password = :password", {"user_name": username, "password": password})
        user = cursor.fetchone()
        if user != None:
            user_name, first_name, last_name, email, gender, password, admin = user
            c_user = User(user_name, first_name, last_name, email, gender, password)
            if admin:
                c_user.make_admin()
            return c_user
    # for user in User.user_list:
    #     if user.user_name == user_name and user.get_password() == password:
    #         return user
        else:
            error("Invalid credentials. Try again.")
            return None

def register():
    print("Please, provide following information-")
    user_name = input("Username: ")
    if not username_validator(user_name):
        error("Username already taken. Try another one.")
        return None
    
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    gender = input("Gender(Male/Female): ")
    password = input("Password: ")
    re_pass = input("Re-type password: ")
    if password != re_pass:
        error("Passwords do not match. Try again.")
        return None
    else:
        success("Account created successfully!")
        user = User(user_name, first_name, last_name, email, gender, password)
        User.username_list.append(user_name)
        User.user_list.append(user)
        create_user(user)
        return user