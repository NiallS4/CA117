class PQ(object):

	def __init__(self):
		self.d = {}
		self.N = 0

	def exch(self, i, j):
		self.d[i], self.d[j] = self.d[j], self.d[i]

	def insert(self, v):
		self.N += 1
		self.d[self.N] = v
		self.swim(self.N)

	def swim(self, k):
		while k > 1 and self.d[k//2] < self.d[k]:
			self.exch(k , k//2)
			k = k//2

	def bigger(self, i, j):
		try:
			return max([i, j], key=self.d.__getitem__)
		except KeyError:
			return i

	def delMax(self):
		v = self.d[1]
		self.exch(1, self.N)
		del(self.d[self.N])
		self.N -= 1
		self.sink(1)
		return v

	def sink(self, k):
		while 2*k <= self.N:
			j = 2*k
			j = self.bigger(j, j + 1)
			if self.d[k] >= self.d[j]:
				break
			self.exch(k, j)
			k = j

	def getMax(self):
		return self.d[1]

	def is_empty(self):
		return self.size() == 0

	def size(self):
		return self.N

def main():

	pq = PQ()
	assert(pq.is_empty() == True)
	assert(pq.size() == 0)
	pq.insert(5)
	pq.insert(6)
	pq.insert(12)
	pq.insert(3)
	pq.insert(15)
	pq.insert(9)
	assert(pq.is_empty() == False)
	assert(pq.size() == 6)
	assert(pq.d[1] == 15)
	assert(pq.d[2] == 12)
	assert(pq.d[3] == 9)
	assert(pq.d[4] == 3)
	assert(pq.d[5] == 5)
	assert(pq.d[6] == 6)
	assert(pq.getMax() == 15)
	assert(pq.delMax() == 15)
	assert(pq.delMax() == 12)
	assert(pq.delMax() == 9)
	assert(pq.delMax() == 6)
	assert(pq.delMax() == 5)
	assert(pq.delMax() == 3)
	assert(pq.is_empty() == True)
	assert(pq.size() == 0)

if __name__ == '__main__':
	main()