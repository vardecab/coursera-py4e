# 4.6 | Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
# Award time-and-a-half [1.5x hourly rate] for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of time-and-a-half in a function called computepay()
# and use the function on to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour
# to test the program (the pay should be 498.75).
# You should use raw_input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.

def computepay():

    hours_string = raw_input("Write your hours: ")
    hours = int(hours_string)

    rate_string = raw_input("Write your hourly rate: ")
    rate = float(rate_string)

    if hours > 40:
        ovt = hours - 40  # overtime hours
        hours_max = 40
        rate_ovt = 1.5 * rate
        pay = (ovt * rate_ovt) + (rate * hours_max)
        return payx
    else:
        rate = 1 * rate
        pay = hours * rate
        return pay

gross_pay = computepay()

print gross_pay