import sys

def build_dictionary(file):
	d = {}
	for line in file:
			english, trans = line.strip().split()
			d[english] = trans
	return d

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

	with open(sys.argv[1], 'r') as f:
		translation = build_dictionary(f)

	for line in sys.stdin:
		l = []
		nums = line.strip().split()
		for n in nums:
			if n in d:
				word = d[n]
				if word in translation:
					l.append(translation[word])
		trans = ' '.join(l)
		print(trans)

if __name__ == '__main__':
	main()