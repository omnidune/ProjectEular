# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

#################################################
# Given any number e.g 12 has a set of factors 1*12, 2*6, 3*4, 4*3, 6*2 and 12*1.
# For 64, it's 1*64 ... 8*8 ... 64*1
# This has a pattern, 1*number ... sqrt(num)*sqrt(num) ... num*1. 
# So in order to determine the primal nature of a number we need to 
# test divisibility up to sqrt(num) only. As set of dividers repeats itself 
# for a non-prime number. 
 
# Time is of essence in this problem, for very large numbers brute 
# force methods work fine, but take too long to compute. So, to mitigate 
# this if we start dividing the given number with 2,3,5,7... then we can run
# a test on each of those results for them being prime numbers, the first 
# one to clear the isprime function gets to be the largest prime number 
# which is a factor of the given number.

import math

def isprime(n):
	m = 2
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

def lrgstpfac(num):
	i = 2
	while True:
		if not num%i:
			numb = num/i
			if isprime(numb):
				return int(numb)
		if i>num/2:
			return
		else:
			i+=1


print(lrgstpfac(600851475143))
