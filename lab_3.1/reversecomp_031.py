import sys

def bsearch(a, q):
	low = 0
	high = len(a)
	while low < high:
		mid = (low + high) // 2
		if a[mid] < q:
			low = mid + 1
		elif a[mid] > q:
			high = mid
		else:
			return a[mid] == q


def main():
	words = [line.strip() for line in sys.stdin]
	words_lower = [line.lower() for line in words]

	print([w for w in words if len(w) >= 5 and bsearch(words_lower, w.lower()[::-1])])


if __name__ == '__main__':
	main()