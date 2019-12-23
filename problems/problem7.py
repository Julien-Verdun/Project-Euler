# Problem 7 : 10001st prime

import math

def is_prime(n):
	"""
	This function returns whether or not an integer is a prime number.
	"""
	if n == 2: 
		return True
	if n == 0 or n == 1 or n%2 == 0:
		return False
	for i in range(3,int(math.sqrt(n))+1,2):
		if n%i == 0:
			return False
	return True

def liste_N_nb_premier(N):
	"""
	This function returns the list of prime number lesser than N.
	"""
	liste = []
	i = 0
	while len(liste) < N:
		if is_prime(i):
			liste.append(i)
		i += 1
	return liste

print(liste_N_nb_premier(10001)[-1])


# Resultat 104743