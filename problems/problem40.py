import numpy as np

# Problem 40 : Champernowne's constant

def dn(n):
	i = 0
	champ = "0."
	while len(champ) <= n+2 :
		i+= 1
		champ += str(i)
	dn = champ[n+1]
	return dn


def dn_liste(liste_n):
	liste_n = np.sort(liste_n)
	liste_dn = []
	i = 0
	j = 0
	champ = "0."
	while len(champ) <= liste_n[-1]+2 :
		i += 1
		champ += str(i)
		if len(champ) >= liste_n[j]+2:
			liste_dn.append(int(champ[liste_n[j]+1]))
			j += 1
	return liste_dn	


def champernowne_constant_product(liste_n):
	liste_dn = dn_liste(liste_n)
	product = 1
	for elt in liste_dn:
		product *= elt
	return product


print(champernowne_constant_product([1,10,100,1000,10000,100000,1000000]))

# Result 210