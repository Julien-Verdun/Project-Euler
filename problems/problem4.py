# Problem 4 : Largest palindrome product


def is_palindrome(number):
	"""
	This function returns whether or not a number is a palindrome number,
	i-e it is the same number read in both direction, e-g 9009.
	"""
    return str(number) == str(number)[::-1]


def largest_palindrome():
	"""
	This function returns the largest palindrom number which
	is the product of 2 3 digits number.
	"""
    I = 999
    J = 999
    largest = 1
    i_max = 999
    j_max = 999
    for i in range(I):
        for j in range(J):
            product = (I-i)*(J-j)
            if product >= largest and is_palindrome(product):
                largest = product
                i_max = I-i
                j_max = J-j
        print("i : ", i)
    return largest, i_max, j_max


print(largest_palindrome())

# Result 906609
