# Problem 6 : Sum square diference

def square_of_sum_minus_sum_of_square(N):
	"""
	This function computes, for a given integer N, the difference beetwen the square of the sum and the sum of squares
	(sum of integer beetwen 1 and N).
	"""
	carre_somme = 0
	somme_carre = 0
	for i in range(1,N+1):
		somme_carre += i**2
		carre_somme += i
	carre_somme = carre_somme**2
	return carre_somme - somme_carre


print(square_of_sum_minus_sum_of_square(100))

# Result 25164150