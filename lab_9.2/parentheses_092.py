from stack_092 import Stack

def matcher(line):

	s = Stack()
	
	left = '({['
	right = ')}]'
	brackets = ['()', '{}', '[]']
	line = line.strip()

	try:
		for e in line:
			if e in left:
				s.push(e)
			else:
				if s.top() + e in brackets:
					s.pop()
		return s.is_empty()
	except:
		return False

import sys

def main():

	for line in sys.stdin:
		print(matcher(line.strip()))

if __name__ == '__main__':
	main()