# Problem 20 : Factorial digit sum

def factorielle(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n*factorielle(n-1)

def sum_digit_factorielle(n):
	factorielle_n = factorielle(n)
	somme = 0
	for elt in str(factorielle_n):
		somme += int(elt)
	return somme


print(sum_digit_factorielle(100))

# Result 648