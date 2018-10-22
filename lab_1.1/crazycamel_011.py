import sys

def camel(s):
	s = s.split()
	a = ''
	for word in s:
		a = a + word[:-1].lower() + word[-1].upper() + ' '
	a = a.strip()
	return a

def main():
	for line in sys.stdin:
		print(camel(line))

if __name__ == '__main__':
	main()