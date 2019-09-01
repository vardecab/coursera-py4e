# http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/

# date

import time

print "Date: " + (time.strftime("%d/%m/%Y"))

# time

from datetime import datetime

t = datetime.now()

print "Time: " + str(t)

print "Time: " + t.strftime('%Y/%m/%d %H:%M:%S')

# random number

import random

print "random#1: ", random.random()

print "random#2: ", random.random()

# random from list

vault = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print "Random letter: " + (random.choice(vault))