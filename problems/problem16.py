# Problem 16 : Power digit sum

def somme_digit_puissance_2(N):
	str_nb = str(2**N)
	somme = 0
	for elt in str_nb:
		somme += int(elt)
	return somme

print(somme_digit_puissance_2(1000))

# Result 1366