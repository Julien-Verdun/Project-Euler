# Problem 17 : Number letter counts


liste_digit_letter = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                      'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
liste_ten_letter = ['twenty', 'thirty', 'forty',
                    'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
liste_other_letter = ['hundred', 'and', 'thousand']


def number_to_value(number, liste_ten_letter=liste_ten_letter, liste_digit_letter=liste_digit_letter, liste_other_letter=liste_other_letter):
    """
	This function takes a number, and 3 lists of words, and calculates
	for this number the number of letter in its writting.
	To do so, the function split the number into units, tens and hundreds
	and do a case disjunction.
	"""
    if number == 0:
        return 0
    elif 1 <= number <= 19:
        return len(liste_digit_letter[number-1])
    elif 20 <= number <= 999:
        number_unit = number % 10
        number_ten = number // 10 % 10
        number_hundreds = number // 100
        if number_ten == 1:
            value = number_to_value(number_ten*10+number_unit)
        else:
            value = number_to_value(number_unit)
            if number_ten not in [0, 1]:
                value += len(liste_ten_letter[number_ten-2])
        if number_hundreds != 0:
            value += len(liste_other_letter[0]) + \
                len(liste_digit_letter[number_hundreds-1])
        if number_hundreds != 0 and (number_ten != 0 or number_unit != 0):
            value += len(liste_other_letter[1])
        return value
    else:
        return len(liste_other_letter[2]) + len(liste_digit_letter[0])


def number_letter_counts():
	"""
	This function calculates the sum of every number's value, for number beetwen
	1 and 1000. It uses the function number_to_value defined above.
	"""
    count = 0
    for i in range(1, 1001):
        print("i : ", i, "value : ", number_to_value(i))
        count += number_to_value(i)
    return count


print(number_letter_counts())

# Result 21124
