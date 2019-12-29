# Problem 5 : Smallest multiple


def is_evenly_divisible(i, N):
    """
    This function returns whether or not the number i
    is evenly divisible (divisible whithout remainder)
    by all of the numbers from 1 to N.
    """
    for j in range(1, N+1):
        if i % j != 0:
            return False
    return True


def smallest_multiple(N):
	"""
	This function returns the smallest number evenly divisible
	by every numbers from 1 to N.
	"""
    i = N
    while not is_evenly_divisible(i, N):
        i += 2
        if i % 10000 == 0:
            print("i : ", i)
    return i

print(smallest_multiple(20))

# Result 232792560
