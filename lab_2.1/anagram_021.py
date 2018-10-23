import sys

def anagram(word1, word2):
	for c in word1:
		if c in word2:
			word2 = word2.replace(c, '', 1)
		else:
			return False
	return word2 == ''

def main():
	for line in sys.stdin:
		[word1, word2] = line.strip().lower().split()
		print(anagram(word1, word2))

if __name__ == '__main__':
	main()