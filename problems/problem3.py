import time
import math


# Problem 3 : Largest prime factor

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


def is_prime_optimise(n, list_nb_prem):
	"""
	This functions does the same thing that is_prime function,
	except that it is optimised in ordered to do use less computation power.
	In fact, we use a list of prime number to find if the number is prime or not,
	if not it has prime factors in the list.
	"""
    for elt in list_nb_prem:
        if n % elt == 0:
            return False
    return True


def liste_nb_premier(N):
	"""
	This function returns the list of prime number lesser than N.
	The function uses the optimised is_prime function.
	"""
    liste = [2]
    for i in range(3, N+1):
        if is_prime_optimise(i, liste):
            liste.append(i)
    return liste


def largest_prime_factor_down(N):
	"""
	This function calculates the largest prime factor of a given number N.
	It starts from 0 and checks if the number is prime and is divided by N.
	"""
    largest = 0
    i = 0
    while i < N:
        if is_prime(i) and N % i == 0:
            largest = i
        i += 1
        if i % 10000 == 0:
            print("Avancement : ", math.floor(10000*i/N)/10000)
    return largest


def largest_prime_factor_up(N, p1=0, p2=100):
	"""
	This function calculates the largest prime factor of a given number N.
	It starts from p2 and decreases until p1 and checks if the number is prime 
	and is divided by N.
	This function is more efficient than the previous one (largest_prime_factor_down).
	"""
    i = p2
    while i > p1:
        if is_prime(i) and N % i == 0:
            return i
        i -= 1
        if i % 10000 == 0:
            print("% : ", math.floor(10000*i/N)/10000)
    return None


nb = 600851475143
p1 = 0
p2 = math.floor(math.sqrt(nb))
# we only check number beetwen 0 and the square root of the number N.
print(largest_prime_factor_up(nb, p1, p2))

# Result 6857
