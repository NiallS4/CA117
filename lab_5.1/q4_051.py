import sys

def main():
	numbers = []
	total = 0
	for num in sys.stdin:
		num = num.strip()
		numbers.append(num)
	
	numbers = [int(n) for n in sorted(numbers)]
	total = sum(numbers)
	N = len(numbers)
	
	mean = total / N

	mode = float(max(set(numbers), key=numbers.count))
	
	if N % 2:
		median = numbers[N//2]
	else:
		median = (numbers[N//2-1] + numbers[N//2]) / 2

	print('Mean: {:.1f}'.format(mean))
	print('Mode: {:.1f}'.format(mode))
	print('Median: {:.1f}'.format(median))

if __name__ == '__main__':
	main()