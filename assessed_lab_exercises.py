def calculator(num1, num2, operator):
    if not isinstance(num1, int): #If input parameter isn't integer, returns message
        return "Invalid input for 1st number"
    if not isinstance(num2, int): #If 2nd input parameter isn't integer, returns message
        return "Invalid input for 2nd number"
    
    if operator == "+": #If statement for adding
        return num1 + num2
    elif operator == "-": #Statement for subtracting
        return num1 - num2
    elif operator == "*": #Statement for multiplying
        return num1 * num2
    elif operator == "/": #Statement for dividing
        if num2 == 0:
            #Error handling as dividing by 0 isnt mathematically possible
            return "Cannot divide by zero"
        else:
            return num1 / num2
    elif operator == "%": #Statement for modulus
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 % num2
    elif operator == ">": #Statement for greater than
        return num1 > num2
    elif operator == ">=": #Statement for greater than or equal to
        return num1 >= num2
    elif operator == "<": #Statement for less than
        return num1 < num2
    elif operator == "<=": #Statement for less than or equal to
        return num1 <= num2
    else:
        #Error handling for if user inputs an operator thats not supported
        return "Invalid operator"

def max_of_three(num1, num2, num3):
    if not isinstance(num1, int): #Error handling to check that each input parameter is an integer
        return "Invalid input for 1st number"
    if not isinstance(num2, int):
        return "Invalid input for 2nd number"
    if not isinstance(num3, int):
        return "Invalid input for 3rd number"
    
    if num1 >= num2: #Will check if num1 is higher than num2
        if num1 >= num3: #Nested for loop checks to see if num1 is higher than num3 - largest number has been identified at this point
            return num1
        else:
            return num3
    #Opposite of first if statement to cover all bases
    elif num2 >= num1: #Can use else, but this helps readability - covers all options for input
        if num2 >= num3: #Works same as previous if loop
            return num2
        else:
            #Needed to avoid blank return if parameters grow in order
            return num3

def winning_numbers(winning_list, guessed_list):
    if not isinstance(winning_list, list): #Error handling to ensure that input parameters are both lists
        return "Invalid input for 1st list"
    if not isinstance(guessed_list, list):
        return "Invalid input for 2nd list"
    for i in winning_list: #Checks each value within each list to ensure that integers are inputted
        if not isinstance(i, int):
            return "Invalid input for value in 1st list"
    for i in guessed_list:
        if not isinstance(i, int):
            return "Invalid input for value in 2nd list"

    #Initialise variable to keep count of correct values
    correct = 0
    #Check each index manually rather than loop as list will always be 3
    if guessed_list[0] in winning_list: #Checks 0 index of guessed list to be in winning list
            correct = correct + 1 #If previous condition satisfied, counter increases by one
    if guessed_list[1] in winning_list: #Repeats same as before but for 1st index
            correct = correct + 1
    if guessed_list[2] in winning_list: #Repeats same as before but for 2nd index
            correct = correct + 1
    if correct == 0: #Returns needed input based on how high the counter was (number of correct guesses)
        return "No"
    elif correct == 1:
        return "Third"
    elif correct == 2:
        return "Second"
    else:
        return "First"

def sum_of_evens(min_num, max_num): 
    if not isinstance(min_num, int): #Checks input parameters to ensure their both integers
        return "Invalid input for 1st number"
    if not isinstance(max_num, int):
        return "Invalid input for 2nd number"
    if min_num > max_num: #Checks to ensure that the first input is smaller than the 2nd input
        return "1st number should be smaller than 2nd"
    if min_num < 0 or max_num < 0: #Ensures that both inputted numbers are more than 0
        return "Both numbers should be positive"
    
    total = 0 #Initiates total counter
    #Loops through all numbers between the given numbers (inclusive)
    for i in range (min_num, max_num + 1):
        #Find even numbers in loop by finding remainder when divided by 2
        if i % 2 == 0:
            total += i #Adds each even number to the total
    return total

def calculate_average(list1): #Have to change variable to list1 as 'list' is datatype
    if not isinstance(list1, list): #Ensures input paramter is a list
        return "Invalid input for list"
    for i in list1:
        if not isinstance(i, int): #Ensures that each value in the list is an integer
            return "Invalid input for value in list"
    
    total = 0 #Initiates 2 counters
    count = 0
    #Loops through list to allow for any length to be accepted
    for i in list1: #Loops through input list and adds each value to the total, and starts counting the number of items in the list
        total += i
        count += 1
    #Define average as separate variable for readability
    average = total / count #Calculated by dividing total by number of values
    return average

def calculate_weekly_pay(hours_worked):
    if not isinstance(hours_worked, int): #Ensures input parameter is an integer
        return "Invalid input for number"
    if hours_worked < 0: #Ensures input is greater than 0
        return "Number should be positive"
    
    money = 0 #Defines money counter at 0
    for i in range(1, hours_worked + 1): #Loops through all the hours worked
        if i <= 35: #For first 35, adds £12 to the total money
            money += 12
        #Could use else here but elif helps readability
        elif i > 35: #For hours over 35, adds £18 to the total money
            money += 18
    #Formatted string used to specify pounds (£)
    return f"£{money}"

def is_prime(number):
    if not isinstance(number, int): #Ensures input parameter is an integer
        return "Invalid input for number"
    if number < 0: #Ensures input parameter is above 0
        return "Number should be positive"

    true = 0
    for i in range(1, number + 1): #Loops through the range from 1 to the number given
        #Checks prime by seeing how many times it divides with remainder 0 (modulus)
        if number % i == 0:
            true += 1

    #Count of 2 determines its prime as its only perfect divides will be 1 and itself
    return true == 2

def are_anagrams(word1, word2):
    if not isinstance(word1, str): #Checks each input paramters are strings
        return "Invalid input for 1st word"
    if not isinstance(word2, str):
        return "Invalid input for 2nd word"
    
    #.upper function converts strings inputted to capitals to make it case-insensitive
    word1 = word1.upper()
    list1 = list(word1) #Converts the word to a list (splits each letter)
    word2 = word2.upper()
    list2 = list(word2)

    length = 0
    #Loops through index of list to allow different sized strings
    for i in range(len(list1)):
        #Checks each letter in word1 with whole of word2
        if list1[i] in list2:
            length += 1
    
    #If counter is same length as 2nd string, it means all letters matched and is an anagram
    return length == len(list2)

def count_vowels(text):
    if not isinstance(text, str): #Ensures input paramter is string
        return "Invalid input for word"

    text = text.lower() #Makes it case-insensitive
    statement = list(text) #Turns the text given into a list which splits the letters
    vowels = 0
    for i in range (len(statement)): #Loops through each letter
        #5 if statements to compare index against each vowel
        if statement[i] == "a": #Checks to see if the letter at index i is a vowel
            vowels += 1 #If condition satisfied, vowel count is incremented
        elif statement[i] == "e": #Repeats same as before
            vowels += 1
        elif statement[i] == "i": #Repeats same as before
            vowels += 1
        elif statement[i] == "o": #Repeats same as before
            vowels += 1
        elif statement[i] == "u": #Repeats same as before
            vowels += 1
    #Can just return the counter as brief only asks for the number
    return vowels

def sort_list(given_list):
    if not isinstance(given_list, list): #Ensures input parmater is a list
        return "Invalid input for list"
    for i in given_list:
        if not isinstance(i, int): #Ensures each value in list is an integer
            return "Invalid input for value in list"
    
    sorted_list = []    
    i = 0
    #Uses while loop which will iterate until the given list is empty
    while i < len(given_list):
        #Finds the smallest number in the given list
        smallest_number = min(given_list)
        #This smallest number is then appended to the sorted list and removed from original to avoid errors
        sorted_list.append(smallest_number)
        given_list.remove(smallest_number)
    return sorted_list

def sum_of_digits(num):
    if not isinstance(num, int): #Ensures the input paramter is an integer
        return "Invalid input for number"
    if num < 0: #Ensures the input paramter is greater than 0
        return "Number should be positive"
    
    #Takes num as an integer and converts it to a string which is then split into each digit in a list
    num_list = list(str(num))
    total = 0
    for i in range(len(num_list)):
        #Converts index of each nubmer back to an integer to add to a total
        total += int(num_list[i])
    return total

def is_palindrome(text):
    if not isinstance(text, str): #Ensures input is a string
        return "Invalid input for word"
    
    #Converts the string input into a list which splits up the letters
    #Uses .upper function too to make it case insensitive
    list_1 = list(text.upper())
    #[::-1] slicing reverses the list
    list_2 = list_1[::-1]
    #Asks for a boolean value to be returned
    return list_1 == list_2

def password_strength(password):
    if not isinstance(password, str): #Ensures input paramter is a string
        return "Invalid input for password"
    
    special_char = False #Sets variables for each condition and sets them to false by default
    length = ""
    capital = False
    #Checks for a special character in the password and sets boolean value to True if satisfied
    if "@" in password or "$" in password or "£" in password:
        special_char = True
    #Checks the length of the password to determine if the length satisfies a weak, medium or strong password
    if len(password) > 10:
        length = "Long"
    elif len(password) >= 6 and len(password) <= 10:
        length = "Mid"
    else:
        length = "Short"
    #Checks for a capital latter in the password and sets boolean value to True if satisfied
    for i in password:
        if i.isupper: #Uses .isupper function
            capital = True
    
    if special_char == True and length == "Long" and capital == True: #Returns strength of password based on what conditions are satisfied
        return "Strong"
    elif special_char == True and length == "Mid" and capital == True:
        return "Medium"
    else:
        return "Weak"

def letter_grade(data_input):
    if not isinstance(data_input, list): #Ensures input paramter is a list
        return "Invalid input for list"
    
    numerator = 0
    denominator = 0
    #Code in necessary formula using for loop and splitting numerator and denominator into separate variables
    for i in data_input:
        numerator += (i["score"] * i["credits"])
        denominator += i["credits"]
    average = numerator / denominator #Calculates average by dividing the numerator and demoninator as it is a fraction

    #Different if condition for each grade
    if average < 50:
        grade = "Grade F"
    elif average >= 50 and average < 60:
        grade = "Grade D"
    elif average >= 60 and average < 70:
        grade = "Grade C"
    elif average >= 70 and average < 90:
        grade = "Grade B"
    elif average >= 90:
        grade = "Grade A"
    
    return (average, grade) #Returns the average and grade as a tuple

def maximum_gap(list1, list2):
    if not isinstance(list1, list): #Ensures both input paramters are lists
        return "Invalid input for 1st list"
    if not isinstance(list2, list):
        return "Invalid input for 2nd list"
    for i in list1: #Ensures all values in both input parameters are integer
        if not isinstance(i, int):
            return "Invalid input for value in 1st list"
    for i in list2:
        if not isinstance(i, int):
            return "Invalid input for value in 2nd list"

    #Finds which list has the largest number to identify which minimum needs to be subtracted
    if max(list1) > max(list2):
        return max(list1) - min(list2)
    elif max(list1) < max(list2):
        return max(list2) - min(list1)

def cipher_text(text, key):
    if not isinstance(text, str): #Ensures the input parmater is a string
        return "Invalid input for text"
    if not isinstance(key, int): #Ensures 2nd input paramter is an integer
        return "Invalid input for key"
    
    string = "" #Sets string as empty by default
    for i in text:
        #ord function gives the ASCII value which the key is then applied to each iteration
        ascii_code = ord(i)
        ascii_code -= key
        ascii_code %= 256 #Keeps it in range
        letter = chr(ascii_code)
        string += letter #Adds each letter to the empty string
    return string

def net_annual_income(gross_salary):
    if not isinstance(gross_salary, int): #Ensures input parameter is an integer
        return "Invalid input for number"
    if gross_salary < 0: #Ensures input paramter is greater than 0
        return "Number should be positive"
    
    if gross_salary <= 12570: #Different if statement for each tax bracket
        return gross_salary
    elif gross_salary > 12570 and gross_salary <= 50270:
        #Subtracts the previous brackets at beginning of each if statement to find tax on only effected amount
        gross_salary -= 12570
        tax = gross_salary * 0.2 #Finds the 20% tax by multipliying salary by 0.2
        gross_salary = (gross_salary - tax) + 12570
        return gross_salary
    elif gross_salary > 50270 and gross_salary <= 125140:
        gross_salary -= 50270
        tax = gross_salary * 0.4 #*0.4 for 40%
        gross_salary = (gross_salary - tax) + 42730 #42730 is maximum from previous brackets added together
        return gross_salary
    elif gross_salary > 125140:
        gross_salary -= 125140
        tax = gross_salary * 0.45#*0.45 for 45%
        gross_salary = (gross_salary - tax) + 87652 #87652 is maximum from previous brackets added together
        return gross_salary

def my_split(my_str, sep):
    if not isinstance(my_str, str): #Ensures that both input paramters are strings
        return "Invalid input for string"
    if not isinstance(sep, str):
        return "Invalid input for separator"
    if len(sep) != 1: #Ensures that the separator is exactly 1 character long
        return "Separator should be 1 character long"
        
    new_str = "" #Defines str and list and empty values
    my_list = []
    for i in my_str:
        #Concatenates to the empty string as long as its not one of the separators
        if i != sep:
            new_str += i
        #When it finds the separator, it appends the current string to the list
        else:
            my_list.append(new_str)
            new_str = "" #Need to reset the string to repeat the loop
    my_list.append(new_str) #Need this line as the final item in string doesn't have separator after
    return my_list

def longest_repetition(text):
    if not isinstance(text, str): #Ensures that the input parameter is a string
        return "Invalid input for string"
    if len(text) < 1: #Ensures that the input parameter isn't empty
        return "String should have characters"

    list_text = list(text) #Converts string to a list
    #Set both current count and final count to 1 with the character being the 0 index
    current_count = 1
    count = 1
    character = list_text[0]
    #Start list from 1st index to end of the list
    for i in range (1, len(list_text)):
        #If current index is the same as previous index, the current count is increased
        if list_text[i] == list_text[i-1]:
            current_count += 1
        #Once the next index is different, it compares the current count to the previous count
        #If the current is higher, the final count is updated and is used in the return
        else:
            if current_count > count:
                character = list_text[i-1] #Previous index is stored into character for the return
                count = current_count
            current_count = 1
    
    #Need this if the repeating characters are at the end of the string
    if current_count > count:
        character = list_text[i-1]
        count = current_count
    return (character, count)

def closest_pair_under_budget(items, budget):
    if not isinstance(items, list): #Ensures first input parameter is a list
        return "Invalid input for list"
    if not isinstance(budget, int): #Ensures budget input parameter is an integer
        return "Invalid input for number"
    for i in items:
        if not isinstance(i, tuple): #Ensures each value inside the list is a tuple
            return "Invalid input for item in list"
    if len(items) < 2: #Ensures that the number of items in list is at least 2 as is necessary for a pair
        return "Not enough items for pair"
    if budget < 0: #Ensures budget isn't negative
        return "Budget should be positive"

    total = 0
    pair = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)): #Starts nested loop one ahead of outer loop
            name_1, price_1 = items[i] #Assigns variable names to tuple pairs
            name_2, price_2 = items[j]
            current_total = price_1 + price_2
            
            #If the current total found in the nested for loop, it updates final total and updates the final pair
            if current_total <= budget and current_total > total:
                total = current_total
                pair = [name_1, name_2]
    return f"{pair} -> total {total}, closest under or equal {budget}" #Uses fortmatted string to return variables within string