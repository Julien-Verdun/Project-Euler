# Problem 37 : Truncatable primes

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


def is_truncatable(nb):
    """
    This function checks whether or not a number is truncatable, i-e
    every sub-number written by removing a front or back number is still
    a prime number. 
    """
    nb = str(nb)
    if is_prime(int(nb)):
        for i in range(1, len(nb)):
            if not is_prime(int(nb[i:])) or not is_prime(int(nb[:len(nb)-i])):
                return False
        return True
    else:
        return False


def truncatable_primes():
    """
    This function looks for the 11 numbers greater than 7 which are truncatable.
    """
    list_tp = []
    i = 8
    while len(list_tp) < 11:
        if is_truncatable(i):
            list_tp.append(i)
        i += 1
        if i % 100 == 0:
            print("i : ", i)
    return list_tp, sum(list_tp)


print(truncatable_primes())

# Result 748317
