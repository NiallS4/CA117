class Triathlete(object):

	def __init__(self, name, tid):
		self.name = name
		self.tid = tid
		self.d = {}
		
	def add_time(self, event, t):
		self.d[event] = t
		
	def get_time(self, event):
		if event in self.d:
			return self.d[event]

	def race_time(self):
		return sum(self.d.values())
		
	def __eq__(self, other):
		return self.race_time() == other.race_time()
		
	def __lt__(self, other):
		return self.race_time() < other.race_time()
	
	def __gt__(self, other):
		return self.race_time() > other.race_time()

	def __str__(self):
		l = []
		l.append('Name: {}'.format(self.name))
		l.append('ID: {}'.format(self.tid))
		l.append('Race time: {}'.format(self.race_time()))
		return '\n'.join(l)

class Triathlon(Triathlete):
	
	def __init__(self):
		self.f = {}
		
	def add(self, ath):
		self.d[ath.tid] = ath
	
	def remove(self, tid):
		if tid in self.d:
			del self.d[tid]
			
	def lookup(self, tid):
		if tid in self.d:
			return self.d[tid]
		else:
			return None

	def best(self):
		return min(self.d.values())

	def worst(self):
		return max(self.d.values())

	def __str__(self):
		output = []
		for k, v in sorted(self.d.items(), key=lambda x: x[1].name):
			output.append('Name: {}'.format(v.name))
			output.append('ID: {}'.format(k))
		return '\n'.join(output)

def main():

	tn = Triathlon()
	t1 = Triathlete('Ian Brown', 21)
	t2 = Triathlete('John Squire', 22)
	t3 = Triathlete('Alan Wren', 23)

	t1.add_time('swim', 100)
	t1.add_time('cycle', 120)
	t1.add_time('run', 150)

	t2.add_time('swim', 300)
	t2.add_time('cycle', 100)
	t2.add_time('run', 200)

	t3.add_time('swim', 50)
	t3.add_time('cycle', 20)
	t3.add_time('run', 10)
	
	tn.add(t1)
	tn.add(t2)
	tn.add(t3)

	print(tn.best())
	print(tn.worst())

if __name__ == '__main__':
	main()