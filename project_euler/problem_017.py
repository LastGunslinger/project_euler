'''

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''
import time
import re

def solve():
	longform = {
		'0': '',
		'00': '',
		'1': 'one',
		'2': 'two',
		'3': 'three',
		'4': 'four',
		'5': 'five',
		'6': 'six',
		'7': 'seven',
		'8': 'eight',
		'9': 'nine',
		'10': 'ten',
		'11': 'eleven',
		'12': 'twelve',
		'13': 'thirteen',
		'14': 'fourteen',
		'15': 'fifteen',
		'16': 'sixteen',
		'17': 'seventeen',
		'18': 'eighteen',
		'19': 'nineteen',
		'20': 'twenty',
		'30': 'thirty',
		'40': 'forty',
		'50': 'fifty',
		'60': 'sixty',
		'70': 'seventy',
		'80': 'eighty',
		'90': 'ninety'
	}

	letters = ''
	for x in range(1, 1001):
		xstr = str(x)
		if len(xstr) == 4:
			letters += 'one thousand'
		if len(xstr) == 3:
			letters += longform[xstr[0]] + ' hundred'
			letters += ' and ' if xstr[1:] != '00' else ''
			xstr = xstr[1:]
		if len(xstr) == 2:
			if xstr in longform:
				letters += longform[xstr] + '\n'
			else:
				letters += longform[xstr[0] + '0']
				letters += '-' if xstr[1] != '0' and xstr[0] != '0' else '' 
				xstr = xstr[1:]
		if len(xstr) == 1:
			letters += longform[xstr] + '\n'

	print(letters)
	letters = re.sub(r'\W', '', letters)
	print(letters)
	return len(letters)

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))