# Problem 53 : Combinatoric selections

def factorielle(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n*factorielle(n-1)

def combinatorics(r,n):
	return factorielle(n)/(factorielle(r)*factorielle(n-r))


def number_value_over_million():
	nb = 0
	for n in range(23,101):
		for r in range(1,n):
			if combinatorics(r,n) > 10**6:
				nb += 1
	return nb

print(number_value_over_million())

# Result 4075