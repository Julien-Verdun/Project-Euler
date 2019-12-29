# Problem 10 : Summation of primes

import math


def is_prime(n):
	"""
	This function returns whether or not an integer is a prime number.
	"""
    if n == 2:
        return True
    if n == 0 or n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def liste_nb_premier(N):
	"""
	This function returns the list of prime number lesser than N.
	"""
    liste = []
    for i in range(N):
        if is_prime(i):
            liste.append(i)
    return liste


N = 2*10**6
print(sum(liste_nb_premier(N)))

# Result 142913828922
