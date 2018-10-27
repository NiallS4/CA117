from stack_092 import Stack

import sys
import math

def calculator(line):

	def plus(a, b):
		return a + b

	def subtract(a, b):
		return a - b

	def product(a, b):
		return a * b

	def divide(a, b):
		return a / b

	def remainder(a, b):
		return a % b

	def power(a, b):
		return a ** b

	def neg(a):
		return -a

	def square(a):
		return a ** 2

	def sqrt(a):
		return math.sqrt(a)

	def log(a):
		return math.log(a)

	binops = {
		'+': plus,
		'-': subtract,
		'*': product,
		'/': divide,
		'%': remainder,
		'**': power,
	}

	uniops = {
		'n': neg,
		's': square,
		'r': sqrt,
		'l': log,
	}

	s = Stack()
	for n in line.split():
		if n.replace('.', '').isdigit():
			s.push(float(n))
		elif n in binops:
			b = s.pop()
			a = s.pop()
			c = float(binops[n](a, b))
			s.push(c)
		elif n in uniops:
			a = s.pop()
			b = uniops[n](a)
			s.push(b)
	return s.top()

def main():

	for line in sys.stdin:
		try:
			a = calculator(line.strip())
			print('{:.2f}'.format(a))
		except IndexError:
			print('Invalid RPN expression')

if __name__ == '__main__':
	main()