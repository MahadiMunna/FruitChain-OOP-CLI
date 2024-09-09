from constants import success, error, make_date, get_int, get_float, get_date

class Fruit(object):

    fruit_list = []
    def __init__(self, fruit_name, price, unit, origin, discount, supply_date, expiry_date):
        self.fruit_name = fruit_name
        self.price = price
        self.unit = unit
        self.origin = origin
        self.discount = discount
        self.supply_date = supply_date
        self.expiry_date = expiry_date
        self.stock_out = False
        Fruit.fruit_list.append(self)

    def make_stock_out(self):
        self.stock_out = True
    
    def make_stock_in(self):
        self.stock_out = False
    @property
    def get_price(self):
        if self.discount > 0:
            return float((self.price - (self.price * self.discount)/100))
        else:
            return float(self.price)

def add_fruit():
    fruit_name = input("Fruit name: ")
    print("Price per unit:", end=" ")
    price = get_float()
    unit = input("Unit (kg/gm/dozen/pcs/etc.): ")
    origin = input("Fruit origin: ")
    print("Discount(0-100):", end=" ")
    discount = get_float()
    print("Supply date (YYYY-MM-DD):", end=" ")
    supply_date = get_date()
    print("Expiry date (YYYY-MM-DD):", end=" ")
    expiry_date = get_date()
    fruit = Fruit(fruit_name, price, unit, origin, discount, supply_date, expiry_date)
    success(f'{fruit.fruit_name} added successfully!')


def view_fruits(stock_out = False):
    for index, fruit in enumerate(Fruit.fruit_list):
        if stock_out == False and fruit.stock_out == False:
            print('='*7 + f' Fruit No: {index+1} ' + '='*7)
            print(f'Fruit name: {fruit.fruit_name}')
            print(f'Price: {fruit.price:.2f}', end=" ")
            if fruit.discount > 0:
                print(f'({fruit.get_price:.2f} at {fruit.discount:.2f}% discount)', end=" ")
            print(f'per {fruit.unit}')
            if fruit.stock_out:
                print(f'Status: Stock out')
            else:
                print(f'Status: Available')
            print(f"Supply Date: {fruit.supply_date}")
            print(f"Expiry Date: {fruit.expiry_date}")
            print('='*len('='*7 + f' Fruit No: {index+1} ' + '='*7)+'\n')
            
        elif stock_out == True and fruit.stock_out == True:
            print('='*7 + f' Fruit No: {index+1} ' + '='*7)
            print(f'Fruit name: {fruit.fruit_name}')
            print(f'Price: {fruit.price:.2f}', end=" ")
            if fruit.discount > 0:
                print(f'({fruit.get_price:.2f} at {fruit.discount:.2f}% discount)', end=" ")
            print(f'per {fruit.unit}')
            if fruit.stock_out:
                print(f'Status: Stock out')
            else:
                print(f'Status: Available')
            print(f"Supply Date: {fruit.supply_date}")
            print(f"Expiry Date: {fruit.expiry_date}")
            print('='*len('='*7 + f' Fruit No: {index+1} ' + '='*7)+'\n')

def user_fruits_view():
    for index, fruit in enumerate(Fruit.fruit_list):
        if fruit.stock_out == False:
            print('='*7 + f' Fruit No: {index+1} ' + '='*7)
            print(f'Fruit name: {fruit.fruit_name}')
            print(f'Price: {fruit.price:.2f}', end=" ")
            if fruit.discount > 0:
                print(f'({fruit.get_price:.2f} at {fruit.discount:.2f}% discount)', end=" ")
            print(f'per {fruit.unit}')
            if fruit.stock_out:
                print(f'Status: Stock out')
            else:
                print(f'Status: Available')
            print('='*len('='*7 + f' Fruit No: {index+1} ' + '='*7)+'\n')

def flash_sale():
    for index, fruit in enumerate(Fruit.fruit_list):
        if fruit.stock_out == False and fruit.discount > 0:
            print('='*7 + f' Fruit No: {index+1} ' + '='*7)
            print(f'Fruit name: {fruit.fruit_name}')
            print(f'Price: {fruit.price:.2f}', end=" ")
            if fruit.discount > 0:
                print(f'({fruit.get_price:.2f} at {fruit.discount:.2f}% discount)', end=" ")
            print(f'per {fruit.unit}')
            if fruit.stock_out:
                print(f'Status: Stock out')
            else:
                print(f'Status: Available')
            print('='*len('='*7 + f' Fruit No: {index+1} ' + '='*7)+'\n')

def update_fruit():
        print('Enter 0 for go back\n')
        print("Enter the fruit no for update:", end=" ")
        no = get_int()
        if no == 0:
            return
        if no not in range(1, len(Fruit.fruit_list)+1):
            error("Invalid fruit no. Try again.")
            return
        fruit = Fruit.fruit_list[no-1]
        print(f'\nFruit Details-\nName: {fruit.fruit_name}\nPrice: {fruit.price:.2f} per {fruit.unit}\nDiscount: {fruit.discount:.2f}\nOrigin: {fruit.origin}\nSupply Date: {fruit.supply_date}\nExpiry Date: {fruit.expiry_date}\n\n')

        print('Enter new details- \n')
        fruit.fruit_name = input("Fruit name: ")
        print("Price per unit:", end=" ")
        fruit.price = get_float()
        fruit.unit = input("Unit (kg/gm/dozen/pcs/etc.): ")
        fruit.origin = input("Fruit origin: ")
        print("Discount(0-100):", end=" ")
        fruit.discount = get_float()
        print("Supply date (YYYY-MM-DD):", end=" ")
        fruit.supply_date = get_date()
        print("Expiry date (YYYY-MM-DD):", end=" ")
        fruit.expiry_date = get_date()
        success(f'Fruit updated successfully!')
    

def manage_stock():
    print("\nChoose your option from below: \n1. Make stock out\n2. See stock out list\nEnter 0 for go back")
    option = get_int()
    if option == 0:
        return
    elif option == 1:
        print("Enter fruit no: ")
        no = get_int()
        if no not in range(1, len(Fruit.fruit_list)+1):
            error("Invalid fruit no. Try again.")
            return
        fruit = Fruit.fruit_list[no-1]
        fruit.make_stock_out()
        success(f'{fruit.fruit_name} is now unavailable')
    
    elif option == 2:
        view_fruits(stock_out=True)
        print("\nChoose your option from below: \n1. Make stock in\nEnter 0 for go back")
        option = get_int()
        if option == 1:
            print("Enter fruit no: ")
            no = get_int()
            if no not in range(1, len(Fruit.fruit_list)+1):
                error("Invalid fruit no. Try again.")
                return
            fruit = Fruit.fruit_list[no-1]
            fruit.make_stock_in()
            success(f'{fruit.fruit_name} is now available')
        elif option == 0:
            return
        else:
            error("Invalid option. Try again.")
    else:
        error("Ops! You have chosen an invalid option!")

