import sys

def capital(s):
	if len(s) > 1:
		return s[0].upper() + s[1:len(s) - 1] + s[len(s) - 1].upper()

def main():
	for line in sys.stdin:
		cs = capital(line.strip())
		if cs:
			print(cs)

if __name__ == '__main__':
	main()