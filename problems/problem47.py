import math

# Problem 47 : Distinct primes factors


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


def unique_decompo_prime_factors(nb, l_nb_p):
    """
    This function take a number and a list of 
    prime number (supposed to go farter than nb)
    and give the different prime numbers involved in 
    the prime decomposition of the number. 
    """
    decompo = []
    for elt in l_nb_p:
        if nb % elt == 0:
            decompo.append(elt)
    return decompo


def is_n_distinct(liste, n):
    """
    This function take a list and returns true if their 
    are  distinct numbers in he list and false otherwise. 
    """
    nb_dist = 0
    list_no_dist = []
    for i in range(len(liste)):
        if liste[i] not in liste[:i] + liste[i+1:]:
            nb_dist += 1
        else:
            if liste[i] not in list_no_dist:
                list_no_dist.append(liste[i])
    nb_dist += len(list_no_dist)
    if nb_dist == n:
        return True
    else:
        return False


def distinct_prime_factor(n):
    """
    This function returns n following numbers 
    and n lists (lists of prime sum decomposition).
    The numbers are the first that have n distinct prime 
    factors in their decompostion.
    """
    i = 0
    list_nb_premier = liste_nb_premier(9**n)
    n_affile = False
    while n_affile == False:
        n_affile = True
        for k in range(n):
            decompo = unique_decompo_prime_factors(i+k, list_nb_premier)
            if not is_n_distinct(decompo, n):
                n_affile = False
                break
        i += 1
    return [i+j-1 for j in range(n)] + [unique_decompo_prime_factors(i+j-1, list_nb_premier) for j in range(n)]


print(distinct_prime_factor(4))

# Result 134043
