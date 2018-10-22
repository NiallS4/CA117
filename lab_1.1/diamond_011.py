import sys

def main():
	n = abs(int(sys.argv[1]))
	s = '*'
	for i in range(1, n + 1):
		print('{:>{}s}'.format(s, n + i - 1))
		s = s + ' *'
	
	s = s[:-4]
	for i in range(n - 1, 0, -1):
		print('{:>{}s}'.format(s, n + i - 1))
		s = s[:-2]
	
if __name__ == '__main__':
	main()