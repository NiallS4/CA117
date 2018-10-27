class Triathlete(object):

	def __init__(self, name, tid):
		self.name = name
		self.tid = tid
		self.d = {}

	def add_time(self, disc, t):
		self.d[disc] = t

	def get_time(self, disc):
		return self.d[disc]

	def __str__(self):
		l = []
		l.append('Name: {}'.format(self.name))
		l.append('ID: {}'.format(self.tid))
		l.append('Race time: {}'.format(sum(self.d.values())))
		return '\n'.join(l)

def main():

	t1 = Triathlete('Ian Brown', 21)

	t1.add_time('swim', 100)
	t1.add_time('cycle', 120)
	t1.add_time('run', 150)

	print('Cycle: {}'.format(t1.get_time('cycle')))
	print(t1)

if __name__ == '__main__':
	main()