# Problem 42 : Coded triangle numbers



def tn(n):
	return n*(n+1)/2

liste_letter_value = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def word_value(word):
	word_value = 0
	for letter in word:
		word_value += (liste_letter_value.index(letter)+1)
	return word_value


def is_triangle_word(word):
	word_val = word_value(word)
	i = 0
	while tn(i) < word_val :
		i += 1
	if tn(i) == word_val :
		return True
	return False

def coded_triangle_numbers(file = "../../words.txt"):
	nb = 0
	with open(file,"r") as word_file:
		words = word_file.read()
	liste_words = words.strip().split(",")
	for elt in liste_words:
		if is_triangle_word(elt[1:len(elt)-1].lower()):
			nb += 1
	return nb

print(coded_triangle_numbers())

# RESULT : 162
