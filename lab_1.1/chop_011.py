import sys

def chop(s):
	return s[1:len(s) - 1]

def main():
	for line in sys.stdin:
		cs = chop(line.strip())
		if cs:
			print(cs)

if __name__ == '__main__':
	main()