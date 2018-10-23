import sys

def main():
	lines = sys.stdin.read().strip()
	lines = lines.split()
	total = []
	for line in lines:
		total.append(line[-1])

	nothing = []
	for n in total:
		if n == '0':
			nothing.append(n)
	prob_nothing = len(nothing) / len(lines) * 100

	onepair = []
	for n in total:
		if n == '1':
			onepair.append(n)
	prob_onepair = len(onepair) / len(lines) * 100

	twopairs = []
	for n in total:
		if n == '2':
			twopairs.append(n)
	prob_twopairs = len(twopairs) / len(lines) * 100

	three = []
	for n in total:
		if n == '3':
			three.append(n)
	prob_three = len(three) / len(lines) * 100

	straight = []
	for n in total:
		if n == '4':
			straight.append(n)
	prob_straight = len(straight) / len(lines) * 100

	flush = []
	for n in total:
		if n == '5':
			flush.append(n)
	prob_flush = len(flush) / len(lines) * 100

	fullh = []
	for n in total:
		if n == '6':
			fullh.append(n)
	prob_fullh = len(fullh) / len(lines) * 100

	four = []
	for n in total:
		if n == '7':
			four.append(n)
	prob_four = len(four) / len(lines) * 100

	straight_flush = []
	for n in total:
		if n == '8':
			straight_flush.append(n)
	prob_straight_flush = len(straight_flush) / len(lines) * 100

	royal_flush = []
	for n in total:
		if n == '9':
			royal_flush.append(n)
	prob_royal_flush = len(royal_flush) / len(lines) * 100

	print('The probability of nothing is {:.4f}%'.format(prob_nothing))
	print('The probability of one pair is {:.4f}%'.format(prob_onepair))
	print('The probability of two pairs is {:.4f}%'.format(prob_twopairs))
	print('The probability of three of a kind is {:.4f}%'.format(prob_three))
	print('The probability of a straight is {:.4f}%'.format(prob_straight))
	print('The probability of a flush is {:.4f}%'.format(prob_flush))
	print('The probability of a full house is {:.4f}%'.format(prob_fullh))
	print('The probability of four of a kind is {:.4f}%'.format(prob_four))
	print('The probability of a straight flush is {:.4f}%'.format(prob_straight_flush))
	print('The probability of a royal flush is {:.4f}%'.format(prob_royal_flush))


if __name__ == '__main__':
	main()