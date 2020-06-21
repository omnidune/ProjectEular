# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

def isprime(n):
	# Returns true if n is prime, False if not.
	m = 2
	if n<=1:
		return False
	while m<=math.sqrt(n):
		if n%m>0 and m == 2:
			m+=1
			continue
		elif n%m>0 and m != 2:
			m+=2
			continue
			# if a number is not divisible by 2, it'll 
			# not be divisible by any even number, 
			# so after 2 testing for even numbers is not optimal  
		else:
			return False
	return True

def primesum(n):
	# Calcualtes sum of all prime number below n.
	num = 2
	lis=[]
	while num<n:
		if isprime(num):
			lis.append(num)
			if num!=2:
				num+=2
			else:
				num+=1
		else:
			num+=1
	# print(lis)
	return(sum(lis))

print(primesum(2000000))
	