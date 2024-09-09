from users import User
from constants import generate_hash, error, success

def username_validator(username):
    if username in User.username_list:
        return False
    else:
        return True
    
def login():
    user_name = input("Enter your username: ")
    input_pass = input("Enter your password: ")
    password = generate_hash(input_pass)
    for user in User.user_list:
        if user.user_name == user_name and user.get_password() == password:
            return user
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
        return User(user_name, first_name, last_name, email, gender, password)