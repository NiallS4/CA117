import sys

def palindrome(s):
	rev_s = s[::-1]
	return s == rev_s

def main():
	for line in sys.stdin:
		s = line.strip().lower()
		for letter in s:
			if not letter.isalnum():
				s = s.replace(letter, '')
		print(palindrome(s))

if __name__ == '__main__':
	main()