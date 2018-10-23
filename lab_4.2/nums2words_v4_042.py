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
	'10' : 'ten',
	'11' : 'eleven',
	'12' : 'twelve',
	'13' : 'thirteen',
	'14' : 'fourteen',
	'15' : 'fifteen',
	'16' : 'sixteen',
	'17' : 'seventeen',
	'18' : 'eighteen',
	'19' : 'nineteen',
	'20' : 'twenty',
	'30' : 'thirty',
	'40' : 'forty',
	'50' : 'fifty',
	'60' : 'sixty',
	'70' : 'seventy',
	'80' : 'eighty',
	'90' : 'ninety',
	'100' : 'one hundred'
	}

	for num in sys.stdin:
		l = []
		numbers = num.strip().split()
		for n in numbers:
			if n in nums:
				n = nums[n]
				l.append(n)
				numbers = ' '.join(l)
			elif n[0] >= '2':
				n = nums[n[0]+'0'] + '-' + nums[n[1]]
				l.append(n)
				numbers = ' '.join(l)
			else:
				n = 'unknown'
				l.append(n)
				numbers = ' '.join(l)
		print(numbers)

if __name__ == '__main__':
	main()