dic = {9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

def numerals(numeral):
	count = 1
	instance = []
	number = []
	if numeral != len(numeral) * numeral[0]:
		for i in range(len(numeral)):
			if len(numeral) == 1:
				return 'I'+numeral
			
			if i == len(numeral) - 2:
				if numeral[i] == numeral[i+1]:
					count += 1
					number.append(count)
					instance.append(numeral[i])
				else:
					number.append(count)
					number.append(1)
					instance.append(numeral[i])
					instance.append(numeral[i+1])
				break		
			else:
				if numeral[i] == numeral[i+1]:
					count += 1
				else:
					number.append(count)
					instance.append(numeral[i])
					count = 1
	else:
		number.append(len(numeral))
		instance.append(numeral[0])

	for i in range(len(number)):
		k = ""
		n = number[i]
		while n > 0:
			for j in dic.keys():
				while n >= j:
					k += dic[j]
					n -= j
		number[i] = k
	
	instanceVar = 0
	numberVar = 0
	final = ["" for i in range((len(instance))*2)]
	for i in range(len(final)):
		if i % 2 == 0:
			final[i] = number[numberVar]
			numberVar += 1
		else:
			final[i] = instance[instanceVar]
			instanceVar += 1	
	return ''.join(final)

def loops(roman, repeats):
	if repeats == 0:
		return roman
	else:
		result = numerals(roman)
		return loops(result, repeats-1)

roman = input("Enter roman numerals: ")
repeats = int(input("Enter number of repetitions: "))

result = loops(roman, repeats)
print("Ones:",result.count('I'))
print("Fives:",result.count('V'))


