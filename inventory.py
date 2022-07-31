# This program reads from the text file inventory.txt and 
# gets an overview of what each stock-taking session entailed
# Author: Chris Bagalwa
# 15/06/2022

# Import the tabulate and pandas module
from tabulate import tabulate
import pandas as pd
# Define the Shoe class
class Shoes:
    # Define the __init__function that is called every time an object is created from the class
    def __init__(self,country,code,product,cost,quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    # Define get_cost function which returns the cost of the shoe
    def get_cost(self):
        return self.cost
    # Define get_quantity function which returns the quantity of the shoes
    def get_quantity(self):
        return self.quantity
    # Define the __str__ function which returns a string representation of a class.
    def __str__(self):
        return self.country + ", " + self.code + ", " + self.product + ", " + str(self.cost) + ", "+ str(self.quantity)
# Define the shoes variable as an empty list
shoes = []
# Define the read_data function that opens and reads data from the inventory.txt file
def read_shoes_data():
    try:
        file = 'inventory.txt'
        with open(file, 'r') as infile:
            infile.readline()
            for line in infile:
                line = line.strip().split(',')
                cost, quantity = float(line[-2]), int(line[-1])
                shoe = Shoes(line[0],line[1],line[2],cost,quantity)
                if shoe not in shoes:
                    shoes.append(shoe)
    except FileNotFoundError:
        print("File not found")
# Define a function that allows the user to capture data about a shoe and 
# use this data to create a shoe object
def capture_shoes():
    cpt_country =  input("Enter country: ")
    cpt_code = input("Enter code: ")
    cpt_product = input("Enter product: ") 
    cpt_cost = int(input("Enter cost: ")) 
    cpt_quantity = int(input("Enter quantity: "))
    # Define the new_show variable
    new_shoe = Shoes(cpt_country, cpt_code,cpt_product, cpt_cost, cpt_quantity)
    # Append the new object inside the shoe list.
    shoes.append(new_shoe)
    # Appending the inventory.txt file
    with open("inventory.txt", "a") as file:
        content = ("\n", cpt_country, ",", cpt_code, ",", cpt_product, ",", str(cpt_cost), ",", str(cpt_quantity))
        file.writelines(content)
        file.close()
# Define the view_all function that will iterate over all the shoes list and
# print the details of the shoes that you return from the __str__ function.
def view_all():
    file = open('inventory.txt', 'r')
    lines = file.readlines()
    # Define list variables as empty lists
    shoe_list = []
    header_list = []
    header_line_splt = lines[0].split(",")
    # Create the list for the table header by eliminating the new line at the end of the string
    for i in range(len(header_line_splt)):
        if(i == 4):
            header_list.append(header_line_splt[4].rstrip("\n"))
            continue
        header_list.append(header_line_splt[i])
    # Iterate through each object,using str() method to read the string returned by __str__() function
    for shoe in shoes:
        shoe_str = str(shoe)
        shoe_list.append(shoe_str.split(","))
    # Use tabulate() method to display the required table
    print(tabulate(shoe_list, headers = header_line_splt))
# Define the re_stock function that find the shoe object with the lowest quantity, 
# which is the shoes that need to be restocked.
def re_stock():
    lowest_quantity = shoes[0]
    for shoe in shoes:
        if shoe.get_quantity() < lowest_quantity.get_quantity():
            lowest_quantity = shoe
    print("Lowest Quantity Details\n")
    print("{:<15} {:<15} {:<20} {:<15} {:<15}"
    .format("Country", "Code", "Product", "Cost", "Quantity"))
    print("{:<15} {:<15} {:<20} {:<15} {:<15}"
    .format(lowest_quantity.country, lowest_quantity.code, lowest_quantity.product, lowest_quantity.cost, lowest_quantity.quantity))
    # Check with the user if they would like to restock
    restock_needed = input("Would you like to restock (yes/no)? ")
    if restock_needed.lower() == "yes":
        update_quantity = int(input("Enter quantity to update: "))
        lowest_quantity.quantity = lowest_quantity.get_quantity() + update_quantity
    else:
        print("No need to update")
# Define the serach_shoe function that search for a shoe from the list using the shoe code and 
# return this object so that it will be printed
def search_shoe(code):
    for shoe in shoes:
        if shoe.code == code:
            return shoe
# Define the value_per_item function that calculates the total value for each item
def value_per_item():
    read_shoes_data()
    print("{:<15} {:<15} {:<20} {:<15} {:<15} {:<15}"
    .format("Country", "Code", "Product", "Cost", "Quantity", "Value"))
    for row, value in enumerate(shoes):
        if row == 0:
            continue
        value.quantity = int(value.quantity)
        value.cost = int(value.cost)
        # Print the information on the console for all the shoes.
        print("{:<15} {:<15} {:<20} {:<15} {:<15} {:<15}"
        .format(value.country, value.code, value.product, value.cost, value.quantity, value.quantity * value.cost))
# Define the highest_qty function that determines the product with the highest quantity 
# and print this shoe as being for sale.
def highest_qty(shoes):
    highest = shoes[0]
    for shoe in shoes:
        if highest.quantity < shoe.quantity: 
            highest = shoe
    return highest
# Main menu
if __name__ == '__main__':
    choice = 0
    while True:
        print('''
1. Read shoes data
2. Capture shoes
3. View all Shoes
4. Restock Shoes
5. Search Shoe
6. Get Total value per item
7. Get product with highest quantity
8. Quit''')
        # Prompt the user to enter their choice
        choice = int(input("Enter choice (eg.: 1): "))
        # Based on user choice call appropriate functions
        if choice == 1:
            read_shoes_data()
        elif choice == 2:
            capture_shoes()
        elif choice == 3:
            print()
            view_all()
        elif choice == 4:
            read_shoes_data()
            re_stock()
        elif choice == 5:
            read_shoes_data()
            code = input("Enter code to be search: ")
            shoe_found = search_shoe(code)
            print("{:<15} {:<15} {:<20} {:<15} {:<15}"
            .format("Country", "Code", "Product", "Cost", "Quantity"))
            print("{:<15} {:<15} {:<20} {:<15} {:<15}"
            .format(shoe_found.country, shoe_found.code, shoe_found.product, shoe_found.cost, shoe_found.quantity))
        elif choice == 6:
            value_per_item()
        elif choice == 7:
            read_shoes_data()
            highest = highest_qty(shoes)
            print("Highest quantity shoe:\n")
            print("{:<15} {:<15} {:<20} {:<15} {:<15}"
            .format("Country", "Code", "Product", "Cost", "Quantity"))
            print("{:<15} {:<15} {:<20} {:<15} {:<15}"
            .format(highest.country, highest.code, highest.product, highest.cost, highest.quantity))
        elif choice == 8:
            print("Thank you.")
            break
        else:
            print("Invalid choice")