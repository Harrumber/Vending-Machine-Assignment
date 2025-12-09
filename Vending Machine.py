import csv #Import csv module to generate csv receipt at the end of the code
with open("receipt.csv", "w", newline = "") as f: #Will clear the receipt of orders from previous runs
    writer = csv.writer(f)
    writer.writerow(["Order Number", "Items Ordered", "Discounts", "Total Spent", "Remaining Balance"]) #Adds the headers to the csv

order_number = 0
def insert_change(): #Function for receiving change
    global balance, order_number
    order_number += 1 #Increase order_number at start of the program
    while True: #Will loop indefinitely as no condition is set
        amount = input("Insert Coin (£2, £1, 50p, 20p) or type 'Done' to finish: ").lower() #.lower() for case-insensitive
        if amount == "2" or amount == "2.00" or amount == "£2": #Allows multiple inputs for improved user experience
            balance += 2 #Updates balance accordingly with the input the user chose
            print(f"Current balance = £{balance:.2f}") #Uses :.2f round feature of f-strings to forces variable to 2 digits
        elif amount == "1" or amount == "1.00" or amount == "£1": #Repeats same for £1
            balance += 1
            print(f"Current balance = £{balance:.2f}")
        elif amount == "50" or amount == "0.5" or amount == "50p": #Repeats same for 50p
            balance += 0.5
            print(f"Current balance = £{balance:.2f}")
        elif amount == "20" or amount == "0.2" or amount == "20p": #Repeats same for 20p
            balance += 0.2
            print(f"Current balance = £{balance:.2f}")
        elif amount == "done": #User chooses once their finished entering coins
            break #Breaks the loop once user wants to
        else:
            print("Invalid input") #Catches invalid inputs that I didn't account for, or coins that aren't accepted

product_dict = { #Defines outside of functions so can be called when needed
    "water": [1.20, 10], #Dictionary for simplicity and efficiency
    "soda": [1.50, 10], #Each item in vending machine gets set its own price and stock level that will be updated accordingly
    "chocolate": [2.50, 5],
    "crisps": [1.40, 8],
    "sandwich": [3.80, 5]
}

def print_menu(): #Utilises muti-line print statement for readability, and is put into function to be called when needed
    print(f"""
        ----- Vending Machine Menu -----
        1. Water - £{product_dict["water"][0]} ({product_dict["water"][1]} in stock)
        2. Soda - £{product_dict["soda"][0]} ({product_dict["soda"][1]} in stock)
        3. Chocolate - £{product_dict["chocolate"][0]} ({product_dict["chocolate"][1]} in stock)
        4. Crisps - £{product_dict["crisps"][0]} ({product_dict["crisps"][1]} in stock)
        5. Sandwich - £{product_dict["sandwich"][0]} ({product_dict["sandwich"][1]} in stock)
        --------------------------------
        Current Balance = £{spent_balance:.2f}
        """) #Updated print to show spent_balance, as well as reading price and stock from the dictionary for each item

#Function for taking user input for item they want to purchase - loops until user orders everything they wanted
#Deducts cost from users balance and deducts 1 from item stock each purchase - prints menu with updated stock levels
def take_order():
    global spent_balance, items_ordered, items_list
    while True: #Will run until user input causes a break
        print_menu() #Calls function to print menu after every successful purchase
        user_order = input("Choose an item you want to order... or type 'Done' to finish: ").upper() #.upper works same as .lower used in order number function
        if user_order == "WATER":
            if spent_balance >= product_dict["water"][0] and product_dict["water"][1] != 0: #Only allows purchase if balance is high enough and stock isnt 0
                product_dict["water"][1] -= 1 #Negates 1 from stock as purchase was successful
                spent_balance -= product_dict["water"][0] #Subtracts price of item from user balance
                print(f"Purchase complete! 1 water for £{product_dict["water"][0]}") #Prints confirmation message for purchase displaying the price
                items_ordered += 1 #Increases a counter for successful purchases to be used for calculating discounts
                items_list.append("Water - £1.20") #Adds string or item ordered and price to a list thats used in receipt
            elif spent_balance < product_dict["water"][0]: #If balance is below price will tell user
                print("Not enough money")
            elif product_dict["water"][1] == 0: #If item is out of stock it won't allow purchase
                print("Out of stock")
        if user_order == "SODA": #Repeats the same for soda
            if spent_balance >= product_dict["soda"][0] and product_dict["soda"][1] != 0:
                product_dict["soda"][1] -= 1
                spent_balance -= product_dict["soda"][0]
                print(f"Purchase complete! 1 soda for £{product_dict["soda"][0]}")
                items_ordered += 1
                items_list.append("Soda - £1.50")
            elif spent_balance < product_dict["soda"][0]:
                print("Not enough money")
            elif product_dict["soda"][1] == 0:
                print("Out of stock")
        if user_order == "CHOCOLATE": #Repeats the same for chocolate
            if spent_balance >= product_dict["chocolate"][0] and product_dict["chocolate"][1] != 0:
                product_dict["chocolate"][1] -= 1
                spent_balance -= product_dict["chocolate"][0]
                print(f"Purchase complete! 1 chocolate for £{product_dict["chocolate"][0]}")
                items_ordered += 1
                items_list.append("Chocolate - £2.50")
            elif spent_balance < product_dict["chocolate"][0]:
                print("Not enough money")
            elif product_dict["chocolate"][1] == 0:
                print("Out of stock")
        if user_order == "CRISPS": #Repeats the same for crisps
            if spent_balance >= product_dict["crisps"][0] and product_dict["crisps"][1] != 0:
                product_dict["crisps"][1] -= 1
                spent_balance -= product_dict["crisps"][0]
                print(f"Purchase complete! 1 crisps for £{product_dict["crisps"][0]}")
                items_ordered += 1
                items_list.append("Crisps - £1.40")
            elif spent_balance < product_dict["crisps"][0]:
                print("Not enough money")
            elif product_dict["crisps"][1] == 0:
                print("Out of stock")
        if user_order == "SANDWICH": #Repeats the same for sandwich
            if spent_balance >= product_dict["sandwich"][0] and product_dict["sandwich"][1] != 0:
                product_dict["sandwich"][1] -= 1
                spent_balance -= product_dict["sandwich"][0]
                print(f"Purchase complete! 1 sandwich for £{product_dict["sandwich"][0]}")
                items_ordered += 1
                items_list.append("Sandwich - £3.80")
            elif spent_balance < product_dict["sandwich"][0]:
                print("Not enough money")
            elif product_dict["sandwich"][1] == 0:
                print("Out of stock")
        if user_order == "DONE":
            print("Order Complete") #Prints confirmation message once user has finished
            break #Breaks loop once user chooses
        if user_order != "WATER" and user_order != "SODA" and user_order != "CHOCOLATE" and user_order != "CRISPS" and user_order != "SANDWICH":
            print("Invalid input") #Accounts for invalid inputs to avoid breaking flow of code

#Define new version of variable to show effect of the discount applied... only largest discount is applied
def applying_discounts():
    global discount, total_spent, new_balance, new_total_spent
    if items_ordered >= 3: #Item ordered counter from previous function used here
        discount = 5 #Sets counter to 5 (purely for readability as this is 5% discount)
    if total_spent > 5: #total_spent variable defined right before functions called by subtracting spent_balance from balance
        discount = 10 #Overwrites counter to 10 as the highest discount needs to be the one thats applied
    if total_spent > 7: #Same thing as previous code
        discount = 15

    if discount == 5:
        new_total_spent *= 0.95 #new_total_spent variable defines before function called as well - initially set to equal total_spent
        new_balance = (balance - new_total_spent) #Updates new_balance variable as to not overwrite original spent balance - however isn't utilised so didn't need
    elif discount == 10:
        new_total_spent *= 0.9 #Applies discount by multipliying total spent by the percentage that they pay after discount
        new_balance = (balance - new_total_spent)
    elif discount == 15:
        new_total_spent *= 0.85 #Applies it to the new_total_spent to not overwrite original amount spent
        new_balance = (balance - new_total_spent)
    else:
        new_balance = spent_balance #If no discounts were applied, updates the variable with no changes
    
    if total_spent > new_total_spent:
        print(f"Total Spent: £{total_spent:.2f} --> £{new_total_spent:.2f}") #Shows the savings made as original balance wasn't overwritten

def odd_order_bonus(total_spent): #Function takes total_spent as input parameter
    global bonus_pound
    bonus_pound = False #Sets condition for if users eligible for bonus pound to False by default
    odd_order_number = (order_number % 2) #See if order number is odd by modulo 2 and remainder is 1
    if total_spent >= 2 and odd_order_number == 1: #Only count an order if £2 was spent and the order number is odd
        bonus_pound = True #Updates variable to True which will be utilised when returning change

def return_change():
    global new_balance, change, bonus_pound, order_number
    odd_order_bonus(total_spent) #Runs the function to deicde if users eligible for bonus £1
    while new_balance >= 2: #Will loop through remaining balance returning £2 coins until balance is below £2
            change += 2 #Utilises new counter to not overwrite remaining balance
            new_balance -= 2 #Subtracts £2 from remaining balance so code can continue
            new_balance = round(new_balance, 2) #Round function changes the variable itself rather than just the way its printed
    while new_balance < 2 and new_balance >= 1: #Repeats for values £2 - £1
            change += 1
            new_balance -= 1
            new_balance = round(new_balance, 2) #Fixes issue with change not returning properly
    while new_balance < 1 and new_balance >= 0.5: #Repeats for values £1 - 50p
            change += 0.5
            new_balance -= 0.5
            new_balance = round(new_balance, 2)
    while new_balance < 0.5 and new_balance >= 0.2: #Repeats for values 50p - 20p (Any change below that is kept)
            change += 0.2
            new_balance -= 0.2
            new_balance = round(new_balance, 2)
    if bonus_pound == True:
        change += 1 #Here the bonus pound is applied based on eligibilty decided by previous function
        print(f"You received a bonus £1 in change!")
    print(f"""Your change is £{change:.2f} and £{new_balance:.2f} was kept
          """) #Utilises multi-line string so that it prints with a gap beneath for improved user readability

def generate_receipt():
    with open("receipt.csv", "a", newline = "") as f: #Appends to the .csv file rather than overwriting the headers
        writer = csv.writer(f)
        writer.writerow([order_number, items_list, f"{discount}%", f"£{new_total_spent:.2f}", f"£{change:.2f}"]) #Appends details of user order with formatted values

def read_receipt():
    with open("receipt.csv", "r") as f: #Accesses the .csv file in read mode
        reader = csv.reader(f)
        rows = list(reader) #Rows defined as the list that the csv reader goes through to act as a counter
        current_row = rows[-1] #Uses slicing to identify last row which will read the latest order
        headers_row = rows[0]  #Will read the first row in the .csv which will always be the headers
        for header, value in zip(headers_row, current_row): #Loops through each column in both rows and prints the value
            print(header)
            print(value)
            print("---") #Prints this to split up receipt to aid readability

def run_vending_machine():
    global balance, items_ordered, spent_balance, items_list, discount, total_spent, new_balance, new_total_spent, change
    while True: #Will loop through orders constantly until breakpoint is reached
        run_condition = input("Type 'START' to begin the process: ").upper() #.upper makes the run_condition case-insensitive
        if run_condition == "START": #Will run all the functions defined previously so the user can use the vending machine
            balance = 0 #Resets balance for each iteration of the code (different orders)
            insert_change()
            items_ordered = 0 #All necesary variables are reset to avoid errors
            spent_balance = balance
            items_list = []
            take_order()
            discount = 0
            total_spent = balance - spent_balance
            new_balance = 0
            new_total_spent = total_spent
            applying_discounts()
            change = 0
            return_change()
            generate_receipt()
            read_receipt()
            if product_dict["water"][1] == 0 and product_dict["soda"][1] == 0 and product_dict["chocolate"][1] == 0 and product_dict["crisps"][1] == 0 and product_dict["sandwich"][1] == 0:
                break #Breakpoint here is only accessed once all stock is empty
    print("Vending Machine is out of stock, come back another time") #Prints message saying vending machine is out of stock and code ends
run_vending_machine()