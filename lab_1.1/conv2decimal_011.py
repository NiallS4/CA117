import sys

def convert(n):
	num = n.strip().split()[0]
	base = n.strip().split()[1]
	decimal = int(num, int(base))
	return decimal

def main():
	for line in sys.stdin:
		print(convert(line))

if __name__ == '__main__':
	main()