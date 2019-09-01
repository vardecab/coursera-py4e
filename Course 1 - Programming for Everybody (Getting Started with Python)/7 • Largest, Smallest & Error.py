# 5.2 | Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message
# and ignore the number.
# Enter the numbers from the book for problem 5.1. Match the desired output as shown:
# Invalid input
# Maximum is 7
# Minimum is 4

largest = None
smallest = None

store = []  # most important thing!

while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done" : break
        else:
           store.append(num)
    except:
        print("Invalid input")  # Python 30[00] syntax

largest=max(store)
smallest=min(store)

print "Invalid input"
print "Maximum is", largest
print "Minimum is", smallest

# code from: https://pr4e.dr-chuck.com/tsugi/mod/pythonauto/index.php?PHPSESSID=dc494bff41ebaa8cec27b6d1652b5c7f