import sys

def main():
	longest = 0
	lines = []
	for line in sys.stdin:
		lines.append(line.strip())
		if len(line) > longest:
			longest = len(line)
	print(lines)

	for i in range(len(lines)):
		print('{:^{}s}'.format(lines[i], longest - 1))

if __name__ == '__main__':
	main()