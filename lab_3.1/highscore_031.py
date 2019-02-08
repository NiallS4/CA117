import sys

def score(a, b, c):
	return (a ** 2) + (b ** 2) + (c ** 2) + (7  * min(a, b, c))

def main():
	for line in sys.stdin:
		words = line.strip().split()
		a, b, c, d = int(words[0]), int(words[1]), int(words[2]), int(words[3])
		
		orig_a = a
		orig_b = b
		orig_c = c

		score1 = score(a, b, c)
		
		a = orig_a
		b += d
		score2 = score(a, b, c)
		
		b = orig_b
		c += d
		score3 = score(a, b, c)

		c = orig_c
		a += d // 2
		c += d // 2
		score4 = score(a, b, c)
		
		print(max(score1, score2, score3, score4))
		
if __name__ == '__main__':
	main()
