import sys

def build_dictionary(file):
	d = {}
	for line in file:
			line = line.strip().split()
			d[line[0]] = line[1]
	return d

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

	file = sys.argv[1]
	with open(file, 'r') as file:
		translation = build_dictionary(file)

	for num in sys.stdin:
		l = []
		numbers = num.strip().split()
		for n in numbers:
			if n in nums:
				n = nums[n]
				if n in translation:
					n = translation[n]
					l.append(n)
					trans = ' '.join(l)
		print(trans)


if __name__ == '__main__':
	main()