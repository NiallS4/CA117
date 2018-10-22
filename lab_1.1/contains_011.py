import sys

def contains(s):
	s = s.split()
	string1 = s[0].upper()
	string2 = s[1].upper()
	for c in string1:
		if c in string2:
			string2 = string2.replace(c, ' ')
		else:
			return False
	return True

def main():
	for line in sys.stdin.readlines():
		print(contains(line.strip()))

if __name__ == '__main__':
	main()