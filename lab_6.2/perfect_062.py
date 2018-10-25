import sys

def sumFac(n):
	return sum(i for i in range(1, (n // 2) + 1) if n % i == 0)

def isPerfect(n):
	sf = sumFac(n)
	return n == sf

def main():
	for num in sys.stdin:
		print(isPerfect(int(num)))

if __name__ == '__main__':
	main()