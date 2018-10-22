import sys

def substring(s):
	s = s.split()
	string1, string2 = s[0].upper(), s[1].upper()
	return string1 in string2

def main():
	for line in sys.stdin.readlines():
		print(substring(line.strip()))

if __name__ == '__main__':
	main()