import sys

def password(s):
	digit = 0
	upper = 0
	lower = 0
	other = 0
	for chars in s:
		if chars.isdigit():
			digit = 1
		elif chars.isupper():
			upper = 1
		elif chars.islower():
			lower = 1
		else:
			other = 1
	return digit + upper + lower + other

def main():
	for line in sys.stdin:
		print(password(line.strip()))

if __name__ == '__main__':
	main()