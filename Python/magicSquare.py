# Sum of each row, column and diagonal add upto same number

def generateSquare(n): 

	# 2-D array with all 
	# slots set to 0 
	magicSquare = [[0 for x in range(n)] for y in range(n)] 

	# initialize position of 1 
	i = n / 2
	j = n - 1
	
	# Fill the magic square 
	# by placing values 
	num = 1
	while num <= (n * n): 
		if i == -1 and j == n: # 3rd condition 
			j, i = n - 2, 0
		else: 

			# next number goes out of 
			# right side of square 
			if j == n: 
				j = 0
				
			# next number goes 
			# out of upper side 
			if i < 0: 
				i = n - 1
				
		if magicSquare[int(i)][int(j)]: # 2nd condition 
			j = j - 2
			i = i + 1
			continue
		else: 
			magicSquare[int(i)][int(j)] = num 
			num = num + 1
				
		j = j + 1
		i = i - 1 # 1st condition 


	# Printing magic square 
	print ("Magic Squre for n =", n) 
	print ("Sum of each row or column", n * (n * n + 1) / 2, "\n") 
	
	for i in range(0, n): 
		for j in range(0, n): 
			print('%2d ' % (magicSquare[i][j]), end = '') 
			
			# To display output 
			# in matrix form 
			if j == n - 1: 
				print() 


# Works only when n is odd 
n = int(input('Enter an odd number: '))
generateSquare(n)

# Example output - 
# Enter an odd number: 5
# Magic Squre for n = 5
# Sum of each row or column 65.0 

#  9  3 22 16 15 
#  2 21 20 14  8 
# 25 19 13  7  1 
# 18 12  6  5 24 
# 11 10  4 23 17
