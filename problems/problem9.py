# Problem 9 : Special Pythagorean triplet

def is_pythagorean_triplet(a,b,c):
	"""
	This function takes 3 integers a, b and c and returns whether or not
	those three numbers are a pythagorean triplet (i-e sum of square of a and b equel square of c).
	"""
	return a**2 + b**2 == c**2

def product_pythagorean_triplet(N):
	"""
	This function returns 3 numbers, if they exist, such that, all 3 numbers are lesser than N, their sum equals
	1000, and they are pythagorean numbers.
	"""
	for a in range(0,N):
		for b in range(a+1,N):
			for c in range(b+1,N):
				if a+b+c == 1000 and is_pythagorean_triplet(a,b,c):
					return a*b*c
	return "N too small"

print(product_pythagorean_triplet(500))

# Resultat 31875000