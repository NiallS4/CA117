import sys

def main():
	word = sys.argv[1]
	N = int(sys.argv[2])
	wordl = list(word)
	x = len(word)
	for i in range(N % x):
		for i in range(len(word)):
			wordl[i], wordl[x-1] = wordl[x-1], wordl[i]
	print(''.join(wordl))
		
if __name__ == '__main__':
	main()