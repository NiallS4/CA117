import sys

def palindrome(s):
	s = s.strip().lower()
	for letter in s:
		if not letter.isalnum():
			s = s.replace(letter, '')
	rev_s = s[::-1]
	return s == rev_s

def main():
	for line in sys.stdin:
		print(palindrome(line))

if __name__ == '__main__':
	main()