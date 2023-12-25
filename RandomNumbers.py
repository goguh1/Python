# Write a script that creates 25 random numbers and inserts into an array then finds
# the largest number.

import random 
#Random module

rn_numbers = random.sample(range(0,100),25)
#Method to generate a list of unique random numbers

print('List:', rn_numbers, '\nMax:', max(rn_numbers))
#prints out a list and the largest
