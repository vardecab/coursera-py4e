# Rewrite your [gross] pay [with overtime] program using try and except
# so that your program handles non-numeric input gracefully.

hours_string = raw_input("Write your hours: ")
try:
    hours = float(hours_string)
except:
    hours = -1

rate_string = raw_input("Write your hourly rate: ")
try:
    rate = float(rate_string)
except:
    rate = -1

if hours == -1 or rate == -1:
    print "Error. Not a correct number format above."
elif hours > 40:
    ovt = hours - 40  # overtime hours
    hours_max = 40
    rate_ovt = 1.5 * rate
    pay = (ovt * rate_ovt) + (rate * hours_max)
    print pay
else:
    rate = rate
    pay = hours * rate
    print pay