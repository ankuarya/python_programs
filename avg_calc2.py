def avg_calc(number_list) :
	total = 0
	list_length = len(number_list)

	if list_length == 0 :
		return total

	for item in number_list :
		total = total + item

	return total/list_length

numbers = []

while(True) :
	val = input('Please enter the number (q to quit) :')

	if val != 'q' :
		numbers.append(int(val))
	else:
		break

avg = avg_calc(numbers)
print()
print('The average of entered numbers is :',avg)


