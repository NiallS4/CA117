import sys

def main():
	ranks = []
	for line in sys.stdin:
		line = line.strip().split(',')
		ranks.append(int(line[-1]))
	
	total = len(ranks)
	
	(nothing, onepair, twopairs, threekind, straight, flush, 
		fhouse, fourkind, sflush, rflush) = ([] for i in range(10))
	
	for c in ranks:
		if c == 0:
			nothing.append(c)
		elif c == 1:
			onepair.append(c)
		elif c == 2:
			twopairs.append(c)
		elif c == 3:
			threekind.append(c)
		elif c == 4:
			straight.append(c)
		elif c == 5:
			flush.append(c)
		elif c == 6:
			fhouse.append(c)
		elif c == 7:
			fourkind.append(c)
		elif c == 8:
			sflush.append(c)
		elif c == 9:
			rflush.append(c) 

	print('The probability of nothing is {:.4f}%'.format((len(nothing) / total) * 100))
	print('The probability of one pair is {:.4f}%'.format((len(onepair) / total) * 100))
	print('The probability of two pairs is {:.4f}%'.format((len(twopairs) / total) * 100))
	print('The probability of three of a kind is {:.4f}%'.format((len(threekind) / total) * 100))
	print('The probability of a straight is {:.4f}%'.format((len(straight) / total) * 100))
	print('The probability of a flush is {:.4f}%'.format((len(flush) / total) * 100))
	print('The probability of a full house is {:.4f}%'.format((len(fourkind) / total) * 100))
	print('The probability of four of a kind is {:.4f}%'.format((len(fourkind) / total) * 100))
	print('The probability of a straight flush is {:.4f}%'.format((len(sflush) / total) * 100))
	print('The probability of a royal flush is {:.4f}%'.format((len(rflush) / total) * 100))

if __name__ == '__main__':
	main()