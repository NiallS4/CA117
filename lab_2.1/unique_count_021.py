import sys

def main():
	unique = []
	for line in sys.stdin:
		s = line.strip().lower()
		for letter in s:
			if not letter.isalnum():
				s = s.replace(letter, ' ')
		words = s.split()
		for word in words:
			if word not in unique:
				unique.append(word)

	print(len(unique))

if __name__ == '__main__':
	main()