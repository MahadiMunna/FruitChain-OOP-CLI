import csv
from datetime import datetime
from constants import generate_hash, error, success, get_int
from db import remove_from_cart_db, create_address, create_order, update_order_status_db, update_payment_status_db, remove_order_db, remove_order_view_for_users


class Order(object):
    orders_list = []
    def __init__(self, user, billing_address, items, total_amount, payment_method, payment_status):
        self.user = user
        self.billing_address = billing_address
        if type(items) == list:
            items_str = ""
            for index, item in enumerate(items):
                items_str+=f'{item.item.fruit_name}x{item.quantity}'
                if index == len(items)-1:
                    items_str+=''
                else:
                    items_str+=', '
            self.items = items_str
        else:
            self.items = items
        self.total_amount = total_amount
        self.payment_method = payment_method
        self.payment_status = payment_status
        self.order_status = None
        self.timestamp = datetime.now()
        text = f'{user.user_name}{items}{total_amount}{payment_method}{self.timestamp}'
        self.order_id = generate_hash(text)
        self.removed = False
        Order.orders_list.append(self)

    def set_order_status(self, status):
        self.order_status = status

class BillingAddress(object):

    def __init__(self, village, post, police_station, district, phone):
        self.village = village
        self.post = post
        self.police_station = police_station
        self.district = district
        self.phone = phone
    def __str__(self):
        return f'{self.village}, {self.post}, {self.police_station}, {self.district}, {self.phone}'


def load_orders_for_user(user):
    for order in Order.orders_list:
        if order.user.user_name == user.user_name and order.removed == False:
            user.orders.append(order)

def place_order(current_user):
    print('Please provide your address information- ')
    billing_address = BillingAddress(
        input("Village: "),
        input("Post: "),
        input("Police station: "),
        input("District: "),
        input("Phone number: "))
    items = [item for item in current_user.cart]
    total_amount = current_user.get_total_amount()
    payment_status = "Pending"
    print("Enter your payment method (1.Card, 2.Mobile Banking, 3.Cash on delivery): ")
    payment_method = get_int()
    if payment_method == 1:
        payment_method = "Card"
        payment_status = "Paid"
    elif payment_method == 2:
        payment_method = "Mobile Banking"
        payment_status = "Paid"
    elif payment_method == 3:
        payment_method = "Cash on delivery"
    else:
        error("Invalid payment method. Please try again.")
        return
    create_address(current_user.user_name, billing_address)
    my_order = Order(current_user, billing_address, items, total_amount, payment_method, payment_status)
    my_order.set_order_status("In Queue")
    current_user.orders.append(my_order)
    create_order(my_order)
    for cart in current_user.cart:
        remove_from_cart_db(current_user, cart)
    current_user.cart = []
    success("Order placed successfully!")
    
def view_orders(current_user):
    if len(current_user.orders) == 0:
        print('='*10 + 'Orders' + '='*10)
        print('You don\'t have any orders yet!')
        print('='*len('='*10 + 'Cart Items' + '='*10))
        return
    else:
        print('='*10 + 'Orders' + '='*10)
        for index, order in enumerate(current_user.orders):
            print(f'{index+1}. {order.items} - {order.total_amount} - {order.payment_status} - {order.order_status} - {order.timestamp}')
        print('='*len('='*10 + 'Cart Items' + '='*10))
    
    print('\nEnter your option:\n1. Cancel order\n2. Remove order from list\nEnter 0 for go back')
    option = get_int()
    if option == 1:
        print('Enter order no for cancel: ')
        no = get_int()
        if no not in range(1, len(current_user.orders)+1):
            error('Invalid order number. Try again.')
            return
        current_user.orders[no-1].order_status = 'Cancelled'
        update_order_status_db(current_user.orders[no-1])
        success('You cancelled the order successfully')
    elif option == 2:
        print('Enter order no for remove from list: ')
        no = get_int()
        if no not in range(1, len(current_user.orders)+1):
            error('Invalid order number. Try again.')
            return
        order = current_user.orders[no-1]
        order.removed = True
        remove_order_view_for_users(order)
        current_user.orders.remove(order)
        success('You removed the order from list successfully')
    elif option == 0:
        return
    else:
        error("Ops! You have chosen an invalid option!")

def manage_orders():
    if len(Order.orders_list) == 0:
        print('='*10 + 'Orders' + '='*10)
        print('No orders available')
        print('='*len('='*10 + 'Cart Items' + '='*10))
        return
    else:
        print('='*10 + 'Orders' + '='*10)
        for index, order in enumerate(Order.orders_list):
            print(f'{index+1}. {order.user.fullname} - {order.items} - {order.total_amount} - {order.payment_method} - {order.order_status} - {order.timestamp}')
        print('='*len('='*10 + 'Cart Items' + '='*10))
    while True:
        print('\nEnter your option:\n1. Update order\n2. Remove order from list\n3. Export to CSV\nEnter 0 for go back')
        option = get_int()

        if option == 1:
            print('Enter order no for update: ')
            no = get_int()
            if no not in range(1, len(Order.orders_list)+1):
                error('Invalid order number. Try again.')
                return
            order = Order.orders_list[no-1]
            print("============Order details============")
            print(f'Customer: {order.user.fullname}\nAddress: {order.billing_address.__str__()}\nOrdered items: {order.items}\nPayable amount: {order.total_amount}\nPayment method: {order.payment_method}\nPayment status: {order.payment_status}\nOrder status: {order.order_status}\nTimestamp: {order.timestamp}')
            print('======================================')
            print('Enter your option:\n1. Update order status\n2. Update payment status\nEnter 0 for go back')
            update_option = get_int()
            if update_option == 1:
                order.order_status = input('In queue/In processing/In transit/Delivered: ')
                update_order_status_db(order)
                success('Order status updated successfully')
            elif update_option == 2:
                order.payment_status = input('Paid/Unpaid: ')
                update_payment_status_db(order)
                success('Payment status updated successfully')
            elif update_option == 0:
                return
            else:
                error("Invalid option. Please try again.")
        elif option == 2:
            print('Enter order no for remove from list: ')
            no = get_int()
            if no not in range(1, len(Order.orders_list)+1):
                error('Invalid order number. Try again.')
                return
            order = Order.orders_list[no-1]
            remove_order_db(order)
            Order.orders_list.remove(order)
            success('You removed the order from list successfully')
        elif option == 3:
            with open('orders.csv', 'w', encoding='UTF8', newline='') as order_file:
                writer = csv.writer(order_file)
                header = ['Customer Name','Billing Address','Ordered Items','Payable Amount','Payment Method','Payment status','Order Status','Timestamp']
                writer.writerow(header)
                for order in Order.orders_list:
                    row = [order.user.fullname, order.billing_address.__str__(), order.items, order.total_amount, order.payment_method, order.payment_status, order.order_status, order.timestamp]
                    writer.writerow(row)
            success('CSV file has been created successfully')
        elif option == 0:
            break
        else:
            error("Invalid option. Please try again.")
        