# Problem 28 : Number spiral diagonals


def sum_spiral_diag(n):
    """
    This function calculates the sum of spiral diagonals.
    """
    somme = 1
    N = n*n
    i = 1  # indique la vauleur des cases
    j = 2  # indique la couche
    while i < N:
        somme += 4*i+10*j
        i += j*4
        j += 1
    return somme


print(sum_spiral_diag(5))
print(sum_spiral_diag(1001))

# Result 948885911
