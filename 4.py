'''
'''

def main():
	results = []
	for num1 in range(999, 99, -1):
		for num2 in range(999, 99, -1):
			result = str(num1 * num2)
			if result == result[::-1] and num1 * num2 not in results:
				results.append(num1 * num2)
	print(results)
	return max(results)

if __name__ == '__main__':
	print(main())