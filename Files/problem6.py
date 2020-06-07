# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# if we remove sqare terms from a binomial expansion 
# we are only left with double the sum of all possible paired multiplied terms

# e.g. (a+b+c+d)^2 - a^2 - b^2 -c^2 -d^2 = 2(ab+ac+ad+bc+bd+cd) 


def difsumsquare(num):
	tot = 0
	for i in range(1,num+1):
		for j in range(i+1, num+1):
			tot = tot + i*j
	return 2*tot

print(difsumsquare(100))