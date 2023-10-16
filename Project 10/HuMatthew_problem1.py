# Define the product information
product_names = [ "onion rings","soft drink", "small fries"]
product_costs = [1.29,0.99, 1.49]
product_quantities = [10, 5, 20]

# Function to search for a product by name
def search_product():
    name = input("Enter a product name: ")

    # Check if the product name exists in the list
    if name in product_names:
        index = product_names.index(name)

        # Print the details of the product
        print("Product found!")
        print("Name: {}\nPrice: {}\nQuantity: {}".format(product_names[index], product_costs[index], product_quantities[index]))
    else:
        print(f"Sorry, we don't sell '{name}'")

# Function to list all products
def list_products():
    print("{:<20} {:<10} {:<10}".format("Product", "Price", "Quantity"))
    for i in range(len(product_names)):
        print("{:<20} {:<10.2f} {:<10}".format(product_names[i], product_costs[i], product_quantities[i]))

# Function to add a new product
def add_product():
    name = input("Enter a product name: ")

    # Check if the product name already exists in the list
    if name in product_names:
        print("Product already exists!")
    else:
        # Get the cost and quantity of the product
        cost = input("Enter a product cost: ")
        while not cost.replace(".", "", 1).isdigit() or float(cost) <= 0:
            cost = input("Invalid cost! Enter a product cost: ")

        quantity = input("Enter a product quantity: ")
        while not quantity.isdigit() or int(quantity) <= 0:
            quantity = input("Invalid quantity! Enter a product quantity: ")
        
        # Add the product to the lists
        product_names.append(name)
        product_costs.append(float(cost))
        product_quantities.append(int(quantity))

        print("Product added.")

# Function to remove a product by name
def remove_product():
    name = input("Enter a product name: ")

    # Check if the product name exists in the list
    if name in product_names:
        index = product_names.index(name)

        # Remove the product from the lists
        product_names.pop(index)
        product_costs.pop(index)
        product_quantities.pop(index)

        print("Product removed.")
    else:
        print("Product not found.")

# Function to update a product by name
def update_product():
    name = input("Enter a product name: ")

    # Check if the product name exists in the list
    if name not in product_names:
        print("Product doesn't exist. Can't update.")
    else:
        index = product_names.index(name)

        # Get the property to update (name, cost or quantity)
        update_type = input("What would you like to update?\n(n)ame, (c)ost or (q)uantity: ")
        while update_type not in ["n", "c", "q"]:
            update_type = input("Invalid option! What would you like to update?\n(n)ame, (c)ost or (q)uantity: ")

        # Update the chosen property of the product
        if update_type == "n":
            new_name = input("Enter a new name: ")
            while new_name in product_names:
                new_name = input("Duplicate name! Enter a new name: ")
            product_names[index] = new_name
            print("Product name has been updated")
        elif update_type == "c":
            new_cost = input("Enter a new cost: ")
            while not new_cost.replace(".", "", 1).isdigit() or float(new_cost) <= 0:
                new_cost = input("Invalid cost! Enter a new cost: ")
            product_costs[index] = float(new_cost)
            print("Product cost has been updated.")
        elif update_type == "q":
            new_quantity = input("Enter a new quantity: ")
            while not new_quantity.isdigit() or int(new_quantity) <= 0:
                new_quantity = input("Invalid quantity! Enter a new quantity: ")
            product_quantities[index] = int(new_quantity)
            print("Product quantity has been updated.")
           
#creating the statements for if a ceratin thing is entered. 

while True:
    action = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")

#if entered q, it will end the program
    if action == 'q':

        print("See you soon!")

        break

#print price quantity and details about product

    elif action == 'l':

        print("Product Price Quantity")

        for i in range(len(product_names)):

            print(f"{product_names[i]} ${product_costs[i]:.2f} {product_quantities[i]}")

#print the product name and change the name

    elif action == 'a':

        name = input("Enter a product name: ")



        while name in product_names:
            print("Duplicate product name")

            name = input("Enter a product name: ")

      
            cost = float(input("Enter the product cost: "))

            quantity = int(input("Enter the product quantity: "))

        else:
            product_names.append(name)

            product_costs.append(cost)

            product_quantities.append(quantity)

            print("Product added")
#if entered r it removes
    elif action == 'r':
        name = input("Enter a product name: ")
        if name in product_names:

            i = product_names.index(name)

            product_names.pop(i)

            product_costs.pop(i)

            product_quantities.pop(i)

            print("Product removed")
        else:
            print("Product not found")

#if entered u, it will change the name or cost aor quantity

    elif action == 'u':

        name = input("Enter a product name: ")

        if name in product_names:

            i = product_names.index(name)

            update = input("What would you like to update?\n(n)ame, (c)ost or (q)uantity: ")

            if update == 'n':

                new_name = input("Enter a new name: ")

                while new_name in product_names:

                    print("Duplicate name!")

                    new_name = input("Enter a new name: ")

                else:
                    product_names[i] = new_name

                    print("Product name has been updated")

            elif update == 'c':

                new_cost = float(input("Enter a new cost: "))

                while new_cost <= 0:

                    print("Invalid cost!")

                    new_cost = float(input("Enter a new cost: "))

                else:

                    product_costs[i] = new_cost

                    print("Product cost has been updated")

            elif update == 'q':

                new_quantity = int(input("Enter a new quantity: "))

                while new_quantity < 0:

                    print("Invalid quantity!")

                    new_quantity = int(input("Enter a new quantity: "))

                else:

                    product_quantities[i] = new_quantity

                    print("Product quantity has been updated")

            while update not in ["n", "c", "q"]:

                print("Invalid option")

            
                
        else:
            print("Product doesn't exist. Can't update.")
            
#if entered e it will give a sum of the products

    elif action == 'e':
                max_price = max(product_costs)

                max_product = [product_names[i] for i, price in enumerate(product_costs) if price == max_price]

                min_price = min(product_costs)

                min_product = [product_names[i] for i, price in enumerate(product_costs) if price == min_price]

                total_value = sum([cost * qty for cost, qty in zip(product_costs, product_quantities)])
                
                print(f"Most expensive product: ${max_price:.2f} ({', '.join(max_product)})")

                print(f"Least expensive product: ${min_price:.2f} ({', '.join(min_product)})")

                print(f"Total value of all products: ${total_value:.2f}")

# if entered s it will search
            
    elif action == 's':

        name = input("Enter a product name: ")

        if name in product_names:
            
            i = product_names.index(name)

            print(f"We sell {product_names[i]} at ${product_costs[i]:.2f} per unit")

        else:
            print(f"Sorry, we don't sell '{name}'")

