'''

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

'''
import time
import pytest

def sort_names():
	names = []
	with open(r'C:\Users\rjoh716\Projects\project_euler\data\p022_names.txt', 'r') as name_file:
		for line in name_file.readlines():
			line = line.replace('\"','').split(',')
			for name in line:
				names.append(str(name).upper())

	return sorted(names)

def get_name_value(name):
	value = 0
	for letter in name:
		value += ord(letter) - 64
	return value

def solve():
	total = 0
	sorted_names = sort_names()
	for i in range(0, len(sorted_names)):
		total += (i + 1)*get_name_value(sorted_names[i])
	return total

def test_main():
	sorted_names = sort_names()
	print(sorted_names)
	assert sorted_names[937] == 'COLIN'
	assert get_name_value(sorted_names[937]) == 49714
	assert get_name_value('REGGIE') == 18 + 5 + 7 + 7 + 9 + 5

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))