# Problem 38 : Pandigital multiples


def is_pandigital(nb):
    """
    This function returns whether or not a number is 
    a 1-9 pandigital number, i-e it can be writted with 
    integers from 1 to 9.
    """
    if len(str(nb)) == 9:
        for i in range(1, 10):
            if str(i) not in str(nb):
                return False
        return True
    else:
        return False


def largest_pandigital_multiples():
    """
    This function returns the largest pandigital number 
    which is a multiple of an integer and a sequence of integer
    (1,2,3,..n)
    """
    largest_number = 0
    for i in range(1, 50000):
        j = 1
        number = i*j
        while len(str(number)) < 9:
            j += 1
            number = int(str(number) + str(i*j))
        if is_pandigital(number) and number > largest_number:
            largest_number = number
    return largest_number


print(largest_pandigital_multiples())

# Result 932718654
