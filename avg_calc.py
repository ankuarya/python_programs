def average_calc(number_list) :
	total = 0
	list_len = len(number_list)
	
	if list_len == 0:
		return total

	for num in number_list :
		total = total + num
	
	return total / list_len


numbers = []

while(True) : 
	val = input('Please Enter a number(q to quit) :')

	if val != 'q' :
		numbers.append(int(val))
	else :
		break

avg = average_calc(numbers)

print()
print('The average of enterd numbers is : ',avg)

