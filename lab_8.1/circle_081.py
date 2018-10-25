class Point(object):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def midpoint(self, other):
		m1, m2 = ((self.x + other.x) / 2), ((self.y + other.y) / 2)
		return Point(m1, m2)

	def __str__(self):
		return '({}, {})'.format(self.x, self.y)

class Circle(object):

	def __init__(self, point=(0, 0), radius=0):
		self.point = point
		self.radius = radius

	def __add__(self, other):
		centre = Point.midpoint(self.point, other.point)
		radius = self.radius + other.radius
		return Circle(centre, radius)

	def __str__(self):
		return 'Centre: {}\nRadius: {}'.format(self.point, self.radius)

def main():
	p1 = Point()
	p2 = Point(4,6)
	c1 = Circle(p1, 10)
	c2 = Circle(p2, 5)
	c3 = c1 + c2
	print(c3)

	p3 = Point(10,10)
	c4 = Circle(p3,15)
	c5 = c2 + c4
	print(c5)
	
if __name__ == '__main__':
	main()
