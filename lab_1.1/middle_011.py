import sys

def middle(s):
	if len(s) % 2:
		pos = len(s) / 2
		middle = s[int(pos)]
		return middle
	else:
		print('No middle character!')

def main():
	for line in sys.stdin:
		ms = middle(line.strip())
		if ms:
			print(ms)

if __name__ == '__main__':
	main()