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

def main():

	t1 = Triathlete('Ian Brown', 21)
	t2 = Triathlete('John Squire', 22)
	t3 = Triathlete('Alan Wren', 23)

	t1.add_time('swim', 100)
	t1.add_time('cycle', 120)
	t1.add_time('run', 150)

	t2.add_time('swim', 300)
	t2.add_time('cycle', 100)
	t2.add_time('run', 200)

	t3.add_time('swim', 150)
	t3.add_time('cycle', 120)
	t3.add_time('run', 100)

	print(t1)
	print(t2)
	print(t3)

	assert(t1 == t3)
	assert(t1 < t2)
	assert(t2 > t3)

if __name__ == '__main__':
	main()