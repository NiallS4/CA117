class Triathlete(object):

	def __init__(self, name, tid):
		self.name = name
		self.tid = tid
		self.d = {}

	def add_time(self, disc, t):
		self.d[disc] = t

	def get_time(self, disc):
		return self.d[disc]

	def __eq__(self, other):
		return sum(self.d.values()) == sum(other.d.values())

	def __gt__(self, other):
		return sum(self.d.values()) > sum(other.d.values())

	def __lt__(self, other):
		return sum(self.d.values()) < sum(other.d.values())

	def __str__(self):
		l = []
		l.append('Name: {}'.format(self.name))
		l.append('ID: {}'.format(self.tid))
		l.append('Race time: {}'.format(sum(self.d.values())))
		return '\n'.join(l)

class Triathlon(Triathlete):

	def __init__(self):
		self.d = {}

	def add(self, t):
		self.d[t.tid] = t

	def remove(self, tid):
		if tid in self.d:
			del self.d[tid]

	def lookup(self, tid):
		if tid in self.d:
			return self.d[tid]
		else:
			return None

def main():

	tn = Triathlon()
	t1 = Triathlete('Ian Brown', 21)
	t2 = Triathlete('John Squire', 22)

	tn.add(t1)
	tn.add(t2)

	t = tn.lookup(21)
	assert(isinstance(t, Triathlete))
	assert(t.name == 'Ian Brown')
	assert(t.tid == 21)

	tn.remove(21)
	t = tn.lookup(21)
	assert(t is None)

if __name__ == '__main__':
	main()