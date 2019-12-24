# Problem 14 : Longest Collatz sequence


def collatz_function(n):
    """
    This function, collatz function, takes a number n and the entire part on the division 
    with 2 if n is even or 3*n+1 is n is odd.
    """
    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1


def longest_collatz_sequence(N):
    """
    This function calculate the longest collatz squence for begining integer lesser than N.
    A collatz sequence finishs when the last number is 1.
    """
    len_max = 0
    i_max = 0
    for i in range(2, N):
        collatz_sequence = [i]
        while collatz_sequence[-1] != 1:
            collatz_sequence.append(collatz_function(collatz_sequence[-1]))
        if len(collatz_sequence)+1 > len_max:
            len_max = len(collatz_sequence)+1
            i_max = i
    return i_max


print(longest_collatz_sequence(10**6))

# Result 837799
