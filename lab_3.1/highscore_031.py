import sys

def main():
	for line in sys.stdin:
		words = line.strip().split()
		a = int(words[0])
		b = int(words[1])
		c = int(words[2])
		d = int(words[3])
		
		x = a
		y = b
		z = c
		a += d
		score1 = (a*a) + (b*b) + (c*c) + (7  * min(a, b, c))
		
		a = x
		b += d
		score2 = (a*a) + (b*b) + (c*c) + (7  * min(a, b, c))
		
		b = y
		c += d
		score3 = (a*a) + (b*b) + (c*c) + (7  * min(a, b, c))

		c = z
		a += d // 2
		c += d // 2
		score4 = (a*a) + (b*b) + (c*c) + (7  * min(a, b, c))
		
		print(max(score1, score2, score3, score4))
		
if __name__ == '__main__':
	main()
