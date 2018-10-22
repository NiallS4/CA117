import sys

def longest_line(s):
	long_len = 0
	for line in s:
		if len(line) > long_len:
			long_len = len(line)
	return long_len
	
def names(s):
	teams = []
	for line in s:
		line = line.split()
		name = ' '.join(line[1:-8])
		teams.append(name)
	return teams

def main():
	lines = []
	for line in sys.stdin:
		line = line.strip()
		lines.append(line)
	
	longest = longest_line(names(lines))
	
	print('{:>s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'
		.format('POS', 'CLUB', longest, 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'PTS'))

	for line in lines:
		tokens = line.split()
		tokens[1:-8] = [' '.join(tokens[1:-8])]
		t = tokens
		print('{:>3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'
			.format(t[0], t[1], longest, t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9]))
		
if __name__ == '__main__':
	main()
	