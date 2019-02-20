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
	'10' : 'ten'
	}

	for line in sys.stdin:
		l = []
		nums = line.strip().split()
		for n in nums:
			if n in d:
				l.append(d[n])
			else:
				l.append('unknown')
		words = ' '.join(l)
		print(words)

if __name__ == '__main__':
	main()