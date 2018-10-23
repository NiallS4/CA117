import sys

def main():
	s = sys.stdin.readlines()
	a = set()
	b = set()
	words = []
	for line in s:
		if len(line.strip()) >= 5:
			a.add(line.strip())
	for c in a:
		f = c
		c = c.lower()
		c = c[::-1]
		d = c.capitalize()
		if c in a or d in a:
			b.add(f)
	for f in b:
		words.append(f)
	words = sorted(words, key=str.lower)
	print(words)

if __name__ == '__main__':
	main()