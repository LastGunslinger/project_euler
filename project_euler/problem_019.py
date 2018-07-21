'''

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''
import time
import pytest

def solve():
	months = {
		'01-January': 31,
		'02-February': None,
		'03-March': 31,
		'04-April': 30,
		'05-May': 31,
		'06-June': 30,
		'07-July': 31,
		'08-August': 31,
		'09-September': 30,
		'10-October': 31,
		'11-November': 30,
		'12-December': 31
	}

	days = [
		'Sunday',
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday'
	]

	first_sundays = 0
	current_day = 2 # epoch day is a Monday
	for year in range(1901,2001):
		if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			months['02-February'] = 29
			print(f'LEAP YEAR - {year}')
		else:
			months['02-February'] = 28
		for month, days_in_month in sorted(months.items()):
			for day in range(1, days_in_month + 1):
				if days[current_day] == 'Sunday' and day == 1: #This is a Sunday
					first_sundays += 1
					print(f'Sunday, {month[3:]} {day}, {year}')
				current_day  = (current_day + 1) % len(days)
	return first_sundays

def test_main():
	pass

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))