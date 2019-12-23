# Problem 56 : Powerful digit sum


def digital_sum(number):
    return sum([int(nb) for nb in list(str(number))])


def powerful_digit_sum():
    max_sum = 1
    max_i, max_j = 100, 100
    for i in range(100):
        for j in range(100):
            max_ab = digital_sum((99-i)**(99-j))
            if max_sum < max_ab:
                max_sum = max_ab
                max_i, max_j = i, j
    return max_sum, 99-max_i, 99-max_j


print(powerful_digit_sum())

# Result 972
