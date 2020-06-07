# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def smalldivnum(largestrange):
	x = largestrange+1
	while True:
		for i in range(1,largestrange+1):
			if x%i != 0:
				x += 1
				break
			if i == largestrange and not x%i:
				return x

print(smalldivnum(20))
