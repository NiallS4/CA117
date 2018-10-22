import sys

es_endings = ['ch', 'sh', 'x', 's', 'z']
vowels = 'aeiou'

def plural(s):
	for chars in s:
		if s[-2:] in es_endings or s[-1] in es_endings:
			return s + 'es'
		elif s[-2:] == 'fe' or s[-1] == 'f':
			s = s.rstrip('fe')
			return s + 'ves'
		elif s[-1] == 'o':
			return s + 'es'
		elif s[-1] == 'y' and s[-2] not in vowels:
			s = s.replace(s[-1], 'ies', 1)
			return s
		else:
			return s + 's'

def main():
	for line in sys.stdin:
		print(plural(line.strip()))

if __name__ == '__main__':
	main()