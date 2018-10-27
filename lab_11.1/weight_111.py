class Weight(object):

	OUNCES_PER_POUND = 16

	def __init__(self, pounds=0, ounces=0):
		self.pounds = pounds
		self.ounces = ounces

	def pounds_to_ounces(self):
		return (self.pounds * self.OUNCES_PER_POUND) + self.ounces

	@classmethod
	def from_ounces(cls, ounces):
		pounds, ounces = divmod(ounces, cls.OUNCES_PER_POUND)
		return cls(pounds, ounces)

	def __eq__(self, other):
		return self.pounds_to_ounces() == other.pounds_to_ounces()

	def __ne__(self, other):
		return self.pounds_to_ounces() != other.pounds_to_ounces()

	def __gt__(self, other):
		return self.pounds_to_ounces() > other.pounds_to_ounces()

	def __lt__(self, other):
		return self.pounds_to_ounces() < other.pounds_to_ounces()

	def __ge__(self, other):
		return self.pounds_to_ounces() >= other.pounds_to_ounces()

	def __le__(self, other):
		return self.pounds_to_ounces() <= other.pounds_to_ounces()

	def __add__(self, other):
		return self.from_ounces(self.pounds_to_ounces() + other.pounds_to_ounces())

	def __iadd__(self, other):
		z = self + other
		self.pounds, self.ounces = z.pounds, z.ounces
		return self

	def __mul__(self, n):
		pounds, ounces = self.pounds * n, self.ounces * n
		return Weight(pounds, ounces)

	def __str__(self):
		return '{} pound(s) and {} ounce(s)'.format(self.pounds, self.ounces)

def main():

	# Create some weights
	w1 = Weight()
	w2 = Weight(6, 4)
	w3 = Weight.from_ounces(100)

	# Confirm all are instances of Weight
	assert(isinstance(w1, Weight))
	assert(isinstance(w2, Weight))
	assert(isinstance(w3, Weight))
	
	# Ounces per pound
	print('Ounces in a pound: {}'.format(Weight.OUNCES_PER_POUND))

	# Display weights
	print('Weights...')
	print(w1)
	print(w2)
	print(w3)

	# Check relations
	assert(w1 != w2)
	assert(w2 == w3)
	assert(w1 < w2)
	assert(w3 > w1)
	assert(w2 >= w3)

	# Addition
	print('Addition...')
	w4 = w2 + w3
	assert(isinstance(w4, Weight))
	print(w4)

	# In-place addition
	print('In-place addition...')
	w2_alias = w2
	w2 += w3
	assert(w2 is w2_alias)
	print(w2)

	# Multiplication
	print('Multiplication...')
	w5 = w3 * 3
	assert(isinstance(w5, Weight))
	print(w5)

if __name__ == '__main__':
	main()