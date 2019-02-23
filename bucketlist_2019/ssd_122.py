import sys

def ssd(num, base):
	# Converts number from base 10 (decimal) to specified base
	converted = []
	while num > 0:
		mod = num % base
		num = num // base
		converted.append(mod)

	sum_digits = sum([n ** 2 for n in converted])
	return sum_digits

def main():
	fail_count = []
	for line_num, line in enumerate(sys.stdin):
		line = line.strip().split()
		try:
			num, base = int(line[0]), int(line[1])
			# Optional fail safe for numbers with base < 2
			if base < 2:
				fail_count.append(str(line_num + 1))
				continue
			print(ssd(num, base))
		except ValueError:
			fail_count.append(str(line_num + 1))

	if len(fail_count) > 0:
		print('Failed to convert line(s): {} '.format(', '.join(fail_count)))

if __name__ == '__main__':
	main()
