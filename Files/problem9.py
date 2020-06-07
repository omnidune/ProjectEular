# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def triMultiply(num):
	for i in range(1, int(num/2)):
		for j in range(i, int(num/2)):
			if i**2 + j**2 == (num-(i+j))**2:
				# print(i, j, num-(i+j))
				return i*j*(num-(i+j))
	return False

print(triMultiply(1000))
