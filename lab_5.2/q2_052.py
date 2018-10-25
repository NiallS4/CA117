import sys

def main():
	for line in sys.stdin:
		line = line.strip()
		new_line = line.lower()
		vowels = 'aeiou'
		for c in new_line:
			if c not in vowels:
				new_line = new_line.replace(c, '')
		if new_line == 'aeiou':
			print(line)

if __name__ == '__main__':
	main()