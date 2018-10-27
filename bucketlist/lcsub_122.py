import sys

def main():
	s1 = sys.stdin.readline()
	s2 = sys.stdin.readline()
	
	lcs = ''
	longest = 0
	
	for i in range(0, len(s1)):
		if s1[i] in s2:
			j = i
			while j < len(s1) and s1[i:j] in s2:
				j += 1
			
			if len(s1[i:j - 1]) > longest:
				lcs = s1[i:j - 1]
				longest = len(lcs)
	
	index = s2.index(lcs)
	
	print(lcs, len(lcs), index)

if __name__ == '__main__':
	main()