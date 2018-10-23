import sys

def main():
	nums = {
	'0' : 'zero',
	'1' : 'one',
	'2' : 'two',
	'3' : 'three',
	'4' : 'four',
	'5' : 'five',
	'6' : 'six',
	'7' : 'seven',
	'8' : 'eight',
	'9' : 'nine',
	'10' : 'ten'
	}

	for num in sys.stdin:
		l = []
		numbers = num.strip().split()
		for n in numbers:
			if n in nums:
				n = nums[n]
				l.append(n)
				numbers = ' '.join(l)
			else:
				n = 'unknown'
				l.append(n)
				numbers = ' '.join(l)

		print(numbers)


if __name__ == '__main__':
	main()