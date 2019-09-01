# 3.1 | Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use raw_input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.

hours_string = raw_input("Write your hours: ")
hours = int(hours_string)

rate_string = raw_input("Write your hourly rate: ")
rate = float(rate_string)

if hours > 40:
    ovt = hours - 40  # overtime hours
    hours_max = 40
    rate_ovt = 1.5 * rate
    pay = (ovt * rate_ovt) + (rate * hours_max)
    print pay
else:
    rate = rate
    pay = hours * rate
    print pay