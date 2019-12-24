# Problem 53 : Combinatoric selections


def factorielle(n):
    """
    This function calculates the factorial of the integer n,
    i-e the product of every integer beetwen 1 and n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorielle(n-1)


def combinatorics(r, n):
	"""
	This function returns the combinatorics of r and n.
	"""
    return factorielle(n)/(factorielle(r)*factorielle(n-r))


def number_value_over_million():
	"""
	This function calculates the first number, combinatorics of the 2 integers, that have a value greter than a million.
	"""
    nb = 0
    for n in range(23, 101):
        for r in range(1, n):
            if combinatorics(r, n) > 10**6:
                nb += 1
    return nb


print(number_value_over_million())

# Result 4075
