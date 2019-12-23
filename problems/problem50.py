# Problem 50 : Consecutive prime sum


def consecutive_prime_sum(N):
	"""
	This function returns for a given number N, the 
	sum, the number nd the list of elements, for the 
	sum of prime numbers that give a prime number and 
	have the largest number of elements.
	"""
	list_nb_premier = liste_nb_premier(N)

	len_sum = 0
	som = 0
	list_nb_prem = []

	for j in range(len(list_nb_premier)):
		for i in range(j+1,len(list_nb_premier)):
			if sum(list_nb_premier[j:i+1]) <= N :
				if is_prime(sum(list_nb_premier[j:i+1])) and i+1-j >= len_sum :		
					som = sum(list_nb_premier[j:i+1])
					len_sum = i+1-j
					list_nb_prem = list_nb_premier[j:i+1]
			else:
				break

	return som,len_sum,list_nb_prem


print(consecutive_prime_sum(1000000))

# Result 997651
