# Problem 48 : Self powers


def self_powers(n):
	if type(n) != int and n < 1:
		print("Wrong n")
	else:
		sum_power = 0
		for i in range(1,n+1):
			sum_power += i**i
	return sum_power


print(self_powers(1000)) 

file = open("../../reponse.txt","w")
file.write("" + str(self_powers(1000))[-10:])
file.close()

# Result check in file ../resolve/response.txt