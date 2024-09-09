# Fruit Chain - Fruit Selling E-Commerce Using CLI

## 1. User Interface
### Command-Line Interface (CLI):
- Users should interact with the system through a CLI.
- The interface should provide clear instructions and prompts to guide users through various operations.
- Implement menus for different functionalities (e.g., Add new fruit, Users management, Profile, Cart, Orders) according to user roles.

## 2. User Authentication and Roles
### Registration:
- Users should be able to register by providing registration information (e.g., username, first name, last name, email, password, etc.).
- User cannot register using the same username that is already registered.
- Passwords should be stored securely (consider using hashing techniques).

### Login:
- Users should log in using their registered credentials.
- Implement a basic session mechanism to maintain user login status during the session.

### Roles:
#### Admin:
- Manage fruit posts.
- Manage stocks.
- Manage users.
- Manage orders.

#### User:
- Can see available fruits.
- Can see fruits with discounts.
- Can add fruit to their cart.
- Can update the cart.
- Can make orders from the cart.
- Can see order details.
- Can cancel orders and remove orders from the list.

## 3. Fruit Management (Admin)
### Add New Fruit:
- Admins should be able to add new fruit posts for sale.
- Required details: fruit name, price, unit, discount, origin, supply date, expiry date.

### Update Fruit Information:
- Admins can update details of existing fruit posts.

### Delete Fruit Post:
- Admins can delete fruit posts anytime.

### Manage Stocks:
- Admin can make a fruit stock out.
- Admin can see stock-out fruit lists.
- Admin can also make stock in.

## 4. Manage Users (Admin)
### Add a New User:
- Admin can add new users by providing user information.
- Required user information: username, first name, last name, email, gender, password.

### Delete a User:
- Admin can delete a user.

### Manage Admin:
- Admin can make a new admin from registered users.
- Admin can remove admin privileges.

## 5. Manage Orders (Admin)
- Admin will be able to see the user who ordered, address, ordered items, total payable amount, payment method, payment status, order status, and timestamp.
- Admin can update order and payment statuses.
- Admin can remove orders from the order list.

## 6. View Fruits (User)
- Users can see available fruits.
- Users can see fruit details.
- There will be a dedicated menu option to see flash sale fruits (fruits with discounts).
- Users can add fruit to the cart for ordering.

## 7. Cart (User)
- Users can see items in the cart that they have added.
- Users can update their cart (e.g., remove items from the cart, change quantity of fruits).
- The total payable amount should be visible in the cart section.
- The order process should start from here.

## 8. Order (User)
- Users can order items in their cart.
- They will have to provide a billing address.
- Required information for billing address: Village, Post, Police station, District, phone number.
- There will be payment methods (e.g., card, mobile banking, cash on delivery).
- Only in cash on delivery, the payment status will show unpaid; for others, it will show paid.

## 9. Profile (Admin and User)
- Users can update profile information here.
- Users can change their password using the previous password.

## 10. Data Structures and Storage
### Data Models:
- Use classes to represent core entities like `User`, `Fruit`, `Cart`, `Order`, and `BillingAddress`.
- Each class should include appropriate attributes and methods for the operations they need to perform.

### Data Storage:
- Use SQLite for persistent storage of data (users, fruits, carts, orders).
- Implement CRUD operations for all entities using SQL queries.

## 11. File Handling
### Export Data:
- Implement functionality for admins to export order information to CSV files.

### Import Data:
- Read fruit posts from a `.txt` file containing fruit information.
- Validate the imported data to ensure it meets the system’s requirements.

## 12. Error Handling
### Input Validation:
- Validate user inputs to prevent errors (e.g., ensure data type correctness, raise a value error if data is incorrect).

### Exception Handling:
- Implement try-except blocks to handle unexpected errors, such as database connection issues or invalid inputs.

### User-Friendly Messages:
- Provide clear and helpful error messages to guide users when something goes wrong.

## 13. Final Integration
### Modular Design:
- Organize the code into modules (e.g., authentication module, fruit management module) for better maintainability.

### Deployment:
- Provide instructions for deploying the system on a local machine.

### User Documentation:
- Write a user manual explaining how to use the system, including screenshots or examples.

## Deliverables:
### Source Code:
- Complete and well-documented Python scripts.

### Database Schema:
- SQL scripts for setting up the necessary tables in the SQLite database.

### Documentation:
- A comprehensive README file with setup instructions, usage guidelines, and system architecture.

### Demonstration:
- A video or presentation showcasing the main features and workflow of the Fruit e-commerce System.
