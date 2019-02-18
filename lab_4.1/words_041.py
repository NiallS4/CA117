import sys
import string

def build_dictionary():
	d = {}
	for line in sys.stdin:
		words = line.lower().strip().split()
		for word in words:
			word = word.strip(string.punctuation)
			if word == '':
				continue
			if word not in d:
				d[word] = 1
			else:
				d[word] += 1
	return d

def main():
	d = build_dictionary()
	for k, v in sorted(d.items()):
		print('{} : {}'.format(k, v))

if __name__ == '__main__':
	main()
