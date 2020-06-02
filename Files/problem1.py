# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
# multiplesOf3and5(10) should return a number.
# multiplesOf3and5(49) should return 543.
# multiplesOf3and5(1000) should return 233168.
# multiplesOf3and5(8456) should return 16687353.
# multiplesOf3and5(19564) should return 89301183.


def mul3and5(num):
	lis = []
	if num <3:
		return 0
	for i in range(num):
		if not i%3 or not i%5:
			lis.append(i)
	return sum(lis)

# print(mul3and5())
