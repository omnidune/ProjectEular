# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10001st prime number?
#################################################


import math

def isprime(num):
	# returns True if num is prime, False if not.
	factor = 2
	while factor<=math.sqrt(num):
		if num%factor > 0 and factor == 2 :
			factor += 1
			continue
		elif num%factor > 0 and factor>2:
			factor += 2
			continue
		else:
			return False
	return True


def primeindex(index):
	# for a given index, 
	# returns the index-th prime number
	number = 1
	ind = 0
	while ind < index:
		if isprime(number):
			ind += 1
			number += 2
			# testing for all odd numbers
		else: 	
			number += 2

	return number-2


print(primeindex(10001))
