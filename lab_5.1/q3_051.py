import sys

def main():
	for line in sys.stdin:
		line = line.strip()
		for c in line:
			if not c.isupper():
				line = line.replace(c, ' ')
		line = line.split()
		print(max(line, key=len))

if __name__ == '__main__':
	main()