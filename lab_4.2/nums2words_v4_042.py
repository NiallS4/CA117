import sys

def main():
	d = {
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

	for line in sys.stdin:
		l = []
		nums = line.strip().split()
		for n in nums:
			if n in d:
				l.append(d[n])
			elif n[0] >= '2':
				l.append(d[n[0] + '0'] + '-' + d[n[1]])
			else:
				l.append('unknown')
		words = ' '.join(l)
		print(words)

if __name__ == '__main__':
	main()