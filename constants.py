import hashlib, datetime

def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()[:10]

def banner(text, width=50):
        print('#' * width)
        print('##'+' '.center(width-4)+'##')
        text = text.center(width-4)
        print(f"##{text}##")
        print('##'+' '.center(width-4)+'##')
        print('#' * width)

def success(text, width=50):
        print('*' * width)
        text = text.center(width-4)
        print(f"**{text}**")
        print('*' * width)

def error(text, width=50):
        print('!' * width)
        text = text.center(width-4)
        print(f"!!{text}!!")
        print('!' * width)

def make_date(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d',).date()

def calculate_total_price(item, quantity):
    return item.get_price*quantity

def get_int():
    while True:
        try:
            return int(input(">  "))
        except ValueError:
            error("Ops! That's not a valid number!")

def get_float():
     while True:
        try:
            return float(input())
        except ValueError:
            error("Ops! That's not a valid number!")

def get_date():
     while True:
        try:
            date = input()
            return make_date(date)
        except ValueError:
            error("Ops! That's not a valid date format!")
     
            
