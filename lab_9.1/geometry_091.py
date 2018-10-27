from math import sqrt

class Shape(object):

	def __init__(self, points):
		self.points = points

	def sides(self):
		l = []
		for i in range(1, len(self.points)):
			l.append(sqrt((self.points[i-1].x - self.points[i].x)**2 + 
				(self.points[i-1].y - self.points[i].y)**2))
		l.append(sqrt((self.points[len(self.points)-1].x - self.points[0].x)**2 + 
			(self.points[len(self.points)-1].y - self.points[0].y)**2))
		return l

	def perimeter(self):
		return sum(self.sides())

class Point(object):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance(self, other):
		distance = sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
		return distance

class Triangle(Shape):

	def area(self):
		sides = self.sides()
		s = (sides[0] + sides[1] + sides[2]) / 2
		return sqrt(s*(s - sides[0])*(s - sides[1])*(s - sides[2]))

class Square(Shape):

	def area(self):
		sides = self.sides()
		return sides[0] * sides[1]

def main():

	t1 = Triangle([Point(0,0), Point(3,4), Point(6, 0)])
	print(t1.sides())
	print(t1.perimeter())
	print(t1.area())

	t2 = Triangle([Point(0,0), Point(4,0), Point(4, 3)])
	print(t2.sides())
	print(t2.perimeter())
	print(t2.area())

	s1 = Square([Point(0,0), Point(5,0), Point(5,5), Point(0,5)])
	print(s1.sides())
	print(s1.perimeter())
	print(s1.area())

if __name__ == '__main__':
	main()