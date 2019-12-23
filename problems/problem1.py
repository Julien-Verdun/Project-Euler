# Problem 1 : Multiples of 3 and 5 

def multiple(a,b):
	"""
	Return True if a is a multiple of b and False instead
	"""
	if a%b == 0 :
		return True
	return False

def sum_multiples(X,Y,N):
	"""
	This function calcutes the sum of all integer multiple of both X and Y and lesser than N
	"""
	somme = 0
	for i in range(N):
		if multiple(i,X) or multiple(i,Y):
			somme += i
	return somme


print(sum_multiples(3,5,10))
print(sum_multiples(3,5,1000))

# Result 233168