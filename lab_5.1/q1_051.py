import sys

def main():
	word = sys.argv[1]
	wordl = list(word)
	for i in range(1, len(word), 2):
		wordl[i-1], wordl[i] = wordl[i], wordl[i-1]
	print(''.join(wordl))

if __name__ == '__main__':
	main()