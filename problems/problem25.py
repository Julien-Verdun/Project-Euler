# Problem 25 :: 1000-digit Fibonacci number

def n_dgt_Fibo(n):
	u = 1
	v = 1
	j = 2
	while len(str(v)) < n :
		u,v=v,u+v
		j+=1
	return j

print(n_dgt_Fibo(1000))

# Result 4782