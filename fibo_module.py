def fibonacci (num) :

	first = 0
	second = 1

	while second < num :
		print second,
		first,second=second, first+second
		#first = second
		#second = first+second
		#print(second)

def fib2 (n) :
	result = []
	a, b = 0,1
	while b < n :
		result.append(b)
		a = b
		b = a + b
	return result