import sys
from math import pi
n = sys.argv[1]

def main():
	print(('{:.{}f}'.format(pi, n)))

if __name__ == '__main__':
	main()