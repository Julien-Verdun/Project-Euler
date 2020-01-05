# Problem 27 : Quadratic primes

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


def quadratic(a, b, n):
	"""
	This function calculates and returns the value
	of the quadratic polynom n**2+a*n+b for given a,
	b and n
	"""
    return n**2 + a*n + b

# List of primes below the value 10**8
list_nb_premier = liste_N_nb_premier(quadratic(1000, 1000, 100))
print("List of primes numbers : ", list_nb_premier[:10])


def number_consecutive_prime(a, b, list_nb_premier=list_nb_premier):
    """
	This function takes the list of primes and two coefficients a and b
	and returns the number of consecutive prime in the quadratic
	poynom values.
	"""
	i = 0
    while quadratic(a, b, i) in list_nb_premier:
        i += 1
    return i


def coeff_max_prim_quadratic():
	"""
	This function tests for every integer coefficients a and b beetwen
	-1000 and 1000, the number of consecutive primes, and keeps the coefficients
	that lead to the maximum number of primes.
	"""
    max_number_coef = 0
    max_coef = []
    for a in range(-1000, 1001):
        print("a : ", a)
        for b in range(-1000, 1001):
            nb_coef = number_consecutive_prime(a, b)
            if nb_coef > max_number_coef:
                max_number_coef = nb_coef
                max_coef = [a, b]
    return max_coef, max_number_coef


print(coeff_max_prim_quadratic())

# Result ([-61, 971],71) => -61*971 = -59231
