# Problem 52 : Permuted multiples

def contain_same_digit(a,b):
	list_a = list(str(a))
	list_b = list(str(b))
	if len(list_a) == len(list_b):
		for elt in list_a:
			if elt not in list_b:
				return False
		return True
	else:
		return False

print(contain_same_digit(125874,251748))


def smallest_permuted_multiple():
	i = 1
	while not (contain_same_digit(i,2*i) and contain_same_digit(i,3*i) and contain_same_digit(i,4*i) and contain_same_digit(i,5*i) and contain_same_digit(i,6*i)):
		i += 1
	return i

print(smallest_permuted_multiple())