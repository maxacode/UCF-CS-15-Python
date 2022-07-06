"""
Lab 1 Exercise
"""
x_string = input("Enter 1st number:")  # Input first number as string
y_string = input("Enter 2nd number:")  # Input second number as string

print("Concatenated: ", x_string+y_string)  # Concatenate both strings


# Converting string inputs to integers
x = int(x_string)
y = int(y_string)

print("Sum: ", x+y)
print("Difference: ", x-y)
print("Multiplication: ", x*y)
print("Division: ", x/y)
print("Remainder: ", x % y)



"""
Lab 2 Exercise
"""
# Create a new script that checks if users can legally purchase an alcoholic beverage

firstName = input("What is your first name? : ")  # Take user input for name
lastName = input("What is your last name? : ")
age = int(input("What is your age? : "))   # Take user input for age

print(f"Your name is {firstName} and you are {age} years old.")  # fstring formatting
print("Your name is {}, and you are {} years old".format(firstName, age))  # .format formatting

# if-else statement to check age
if age >= 21:
    print("You can buy alcoholic beverages")
else:
    print('Sorry you are too young to buy alcohol')



"""
Lab 3 Exercise
"""
# Write code that asks the user to provide a score for an exam as input and checks what grade
# the score is associated with.

grade = int(input("Enter a grade: ")) # Grade is converted to an integer

# if statement to check is 90 or greater
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 65:
    print("D")
elif grade >= 0:
    print("F")
else:
    print("ERROR: Grades cannot be negative numbers or words.")


"""
Lab 4 Exercise
"""

# Construct an interactive script that returns which service is associated with which port number.

protocolsDict = {
    'FTP': '20, 21',
    'SSH': '22',
    'Telnet': '23',
    'SMTP': '25',
    'DNS': '53',
    'DHCP': '67, 68',
    'POP3': '110',
    'IMAP4': '143',
    'NetBIOS': '137, 138, 139',
    'LDAP': '389',
    'SMB': '445',
    'HTTP': '80',
    'HTTPS': '443',
    'MySQL': '3306'
}
# Added .upper() so it changes input to uppercase to be read in the dictionary
question = input("Which protocol do you want to know the port number for? : ").upper()

if question in protocolsDict.keys():
    answer = protocolsDict[question]
    print(f"The port number for {question} is {answer}.")
else:
    print(f"The port number for {question} cannot be found.")


