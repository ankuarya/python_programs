sentence = input('Please enter a sentence : ')
words=sentence.split(' ')

char_count_dict={}

for word in words :
	characters = list(word)
	for char in characters :
		if char in char_count_dict :

			char_count_dict[char] += 1
		else:
			char_count_dict[char] = 1

sorted_keys = sorted(char_count_dict.keys())
for key in sorted_keys:
	value = char_count_dict[key]
	print('found:',key,value,'times')
