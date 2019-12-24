# Problem 29 : Distinct powers


def distinct_powers(a_max, b_max):
    """
    This function calculates the number of distinc powers (a**b) 
    for a beetwen 1 and a_max and b beetwen 1 and b_max. 
    """
    liste_powers = []
    for i in range(2, a_max+1):
        for j in range(2, b_max+1):
            if i**j not in liste_powers:
                liste_powers.append(i**j)
    return len(liste_powers)


print(distinct_powers(100, 100))

# Result 9183
