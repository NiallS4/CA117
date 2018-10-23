from collections import namedtuple

def show_student(s):
	print('{:>{:d}s}: {}'.format('First name', 10, s[0]))
	print('{:>{:d}s}: {}'.format('Surname', 10, s[1]))
	print('{:>{:d}s}: {}'.format('ID', 10, s[2]))

Student = namedtuple('Student', ['firstname', 'surname', 'id'])