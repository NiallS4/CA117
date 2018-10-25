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

	def __iadd__(self, other):
		z = self + other
		self.goals, self.points = z.goals, z.points
		return self

	def __isub__(self, other):
		z = self - other
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

	# Equality / inequality
	print('Equality / inequality...')
	print(s1 == s2)
	print(s1 != s2)
	print(s2 == s3)
	print(s2 != s3)
	print(s3 == s4)
	print(s3 != s4)

	# Greater than / less than
	print('Greater than / less than...')
	print(s1 > s2)
	print(s2 < s3)

	# Greater than or equal to / less than or equal to
	print('Greater than or equal to / less than or equal to...')
	print(s1 >= s2)
	print(s2 >= s3)
	print(s3 >= s2)
	print(s2 >= s4)
	print(s4 >= s2)
	print(s1 <= s2)
	print(s2 <= s3)
	print(s3 <= s2)
	print(s2 <= s4)
	print(s4 <= s2)

	# Addition
	print('Addition...')
	s6 = s3 + s4
	print(s6)

	# Subtraction
	print('Subtraction...')    
	s6 = s2 - s5
	print(s6)

	# In-place addition
	print('In-place addition...')
	s2alias = s2
	s2 += s5
	print(s2)
	print(s2 > s5)
	print(s2 == s2alias)

	# In-place subtraction
	print('In-place subtraction...')
	s2 -= s5
	print(s2)
	print(s2 > s5)
	print(s2 == s2alias)

	# Sorting
	print('Sorting...')    
	for s in sorted([s1, s2, s3, s4, s5, s6], reverse=True):
		print(s)

if __name__ == '__main__':
	main()