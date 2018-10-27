from priority_queue_112 import PQ
import sys

def main():

	pq = PQ()
	m = int(sys.argv[1])
	for num in sys.stdin:
		pq.insert(int(num.strip()))

	for i in range(pq.size()-m):
		pq.delMax()

	l = []
	for i in range(m):
		l.append(pq.getMax())
		pq.delMax()

	for n in l:
		print(n)

if __name__ == '__main__':
	main()