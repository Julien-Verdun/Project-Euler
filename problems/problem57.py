# Problem 57 : Square root convergents


def frac(n):
    if n > 1:
        return 1/(2+frac(n-1))
    else:
        return 1/2


def square_root_approx(n):
    return 1 + frac(n)


def square_root_convergents(n):
    i = 0
    nb_frac = 0
    num = 1
    den = 2
    while i < n:
        if i % 10 == 0:
            print(i, " : ", den + num, " / ", den)
        if len(str(den + num)) > len(str(den)):
            nb_frac += 1
        i += 1
        num, den = den, 2*den+num
    return nb_frac


print(square_root_convergents(1000))
