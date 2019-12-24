# Problem 48 : Self powers


def self_powers(n):
    """
    This function calculates the sum of integer's power integer (i**i) for
    integer beetwen 1 and n.  
    """
    if type(n) != int and n < 1:
        print("Wrong n")
    else:
        sum_power = 0
        for i in range(1, n+1):
            sum_power += i**i
    return sum_power


print(self_powers(1000))

# The result is written on a text file in order to read it.
file = open("problem48_response.txt", "w")
file.write("" + str(self_powers(1000))[-10:])
file.close()
