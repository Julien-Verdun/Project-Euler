# Problem 20 : Factorial digit sum


def factorielle(n):
    """
    This function calculates the factorial of the integer n,
    i-e the product of every integer beetwen 1 and n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorielle(n-1)


def sum_digit_factorielle(n):
	"""
	This function returns the sum of every digits in the number factorial n.
	"""
    factorielle_n = factorielle(n)
    somme = 0
    for elt in str(factorielle_n):
        somme += int(elt)
    return somme


print(sum_digit_factorielle(100))

# Result 648
