# Problem 2 : Even Fibonacci numbers

def sum_even_fibonacci_numbers(N):
	"""
	Given an integer N, this function compute the sum of fibonacci's terms lesser or equal to N.
	"""
	u = 1
	v = 2
	liste_even_fibonacci = [2]
	while v <= N:
		u,v = v,u+v
		if v%2 == 0:
			liste_even_fibonacci.append(v)
	return sum(liste_even_fibonacci)

print(sum_even_fibonacci_numbers(4*10**6))

# Result 4613732