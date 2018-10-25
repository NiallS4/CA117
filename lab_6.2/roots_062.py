import sys
from math import sqrt

def get_roots(a, b, c):
	try:
		r1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
		r2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
		return [r1, r2]
	except:
		return None

def main():
	for line in sys.stdin:
		a, b, c = line.strip().split()
		roots = get_roots(int(a), int(b), int(c))
		if roots != None:
			print('r1 = {}, r2 = {}'.format(roots[0], roots[1]))
		else:
			print(roots)

if __name__ == '__main__':
	main()