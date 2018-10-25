class Score(object):

	def __init__(self, goals=0, points=0):
		self.goals = goals
		self.points = points
		
	def __gt__(self, other):
		return (self.goals*3 + self.points) > (other.goals*3 + other.points)

	def __ge__(self, other):
		return (self.goals*3 + self.points) >= (other.goals*3 + other.points)

	def __lt__(self, other):
		return (self.goals*3 + self.points) < (other.goals*3 + other.points)

	def __le__(self, other):
		return (self.goals*3 + self.points) <= (other.goals*3 + other.points)

	def __eq__(self, other):
		return (self.goals*3 + self.points) == (other.goals*3 + other.points)

	def __add__(self, other):
		goals, points = (self.goals + other.goals), (self.points + other.points)
		return Score(goals, points)

	def __sub__(self, other):
		goals, points = (self.goals - other.goals), (self.points - other.points)
		return Score(goals, points)

	def __mul__(self, n):
		goals, points = self.goals * n, self.points * n
		return Score(goals, points)

	def __rmul__(self, n):
		goals, points = self.goals * n, self.points * n
		return Score(goals, points)

	def __iadd__(self, other):
		z = self + other
		self.goals, self.points = z.goals, z.points
		return self

	def __isub__(self, other):
		z = self - other
		self.goals, self.points = z.goals, z.points
		return self

	def __imul__(self, other):
		z = self * other
		self.goals, self.points = z.goals, z.points
		return self

	def __str__(self):
		return '{} goal(s) and {} point(s)'.format(self.goals, self.points)

def main():

	# Create some instances of Score
	s1 = Score()
	s2 = Score(3, 12)
	s3 = Score(4, 9)
	s4 = Score(2, 11)
	s5 = Score(1, 1)

	# Display
	print('Display...')
	print(s1)
	print(s2)
	print(s3)
	print(s4)

	# Multiplication
	print('Multiplication...')
	s2 = s2 * 2
	print(s2)
	print(s2 > s3)

	# Right multiplication
	print('Right multiplication...')
	s2 = 2 * s2
	print(s2)
	print(s2 > s3)

	# In-place multiplication
	print('In-place multiplication...')
	s2alias = s2
	s2 *= 2
	print(s2)
	print(s2alias)
	print(s2 == s2alias)

if __name__ == '__main__':
	main()