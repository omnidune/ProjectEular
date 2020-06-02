# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

#################################################
# So ... largest factor of a number is around half of that number.
# Time is of essence in this problem, for very large numbers brute 
# force methods work fine, but take too long to compute. So, to mitigate 
# this if we start dividing the given number with 2,3,4… then we can run
# a test on each of those results for them being prime numbers, the first 
# one to clear the isprime function gets to be the largest prime number 
# which is a factor of the given number.

def isprime(n):
	m = 2
	while m<n/2:
		if n%m>0:
			m+=1
			continue
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
