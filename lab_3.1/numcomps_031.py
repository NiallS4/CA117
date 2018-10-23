import sys

N = int(sys.argv[1])

def three(n):
	return [n for n in range(1, N + 1) if n % 3 == 0]

def three_square(n):
	return [n ** 2 for n in range(1, N + 1) if n % 3 == 0]

def four_double(n):
	return [n*2 for n in range(1, N + 1) if n % 4 = =0]

def three_or_four(n):
	return [n for n in range(1, N + 1) if n % 3 == 0 or n % 4 == 0]

def three_and_four(n):
	return [n for n in range(1, N + 1) if n % 3 == 0 and n % 4 == 0]

def replace(n):
	return ['X' if n % 3 = =0 else n for n in range(1, N + 1)]

def prime(n):
	return [n for n in range(2, N + 1) if all(n % x != 0 for x in range(2, n))]

def main():
	print('Multiples of 3: {}'.format(three(N)))
	print('Multiples of 3 squared: {}'.format(three_square(N)))
	print('Multiples of 4 doubled: {}'.format(four_double(N)))
	print('Multiples of 3 or 4: {}'.format(three_or_four(N)))
	print('Multiples of 3 and 4: {}'.format(three_and_four(N)))
	print('Multiples of 3 replaced: {}'.format(replace(N)))
	print('Primes: {}'.format(prime(N)))

if __name__ == '__main__':
	main()