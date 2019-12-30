# Problem 30 : Digit fifth powers


def somme_nth_dgt_powers(n, limit=10**7):
	"""
	This function takes an integer n, a limit number of iterations
	and returns the list of numbers, lesser than limit, such that
	the sum of their n-th power digit equal this number, and also
	the sum of also such number.
	"""
    i = 2
    liste_nb = []
    while i < limit:
        sum_nth_digit = sum([int(digit)**n for digit in str(i)])
        if i == sum_nth_digit:
            liste_nb.append(i)
        if i % 1000 == 0:
            print("i : ", i)
        i += 1
    return liste_nb, sum(liste_nb)


print(somme_nth_dgt_powers(5, 1000000))

# Result 443839
