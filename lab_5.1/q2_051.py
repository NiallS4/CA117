import sys

def main():
	for line in sys.stdin:
		line = line.strip()
		new_line = line.lower()
		letters = 'evil'
		for c in new_line:
			if c not in letters:
				new_line = new_line.replace(c, '')
		if new_line == 'evil':
			print(line)

if __name__ == '__main__':
	main()