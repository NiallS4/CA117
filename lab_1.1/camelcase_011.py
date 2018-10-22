import sys

def camel(s):
	s = s.split()
	a = ''
	for word in s:
		a = a + word.capitalize() + ' '
	a = a.strip()
	return a

def main():
	for line in sys.stdin:
		cc = camel(line)
		print(cc)

if __name__ == '__main__':
	main()