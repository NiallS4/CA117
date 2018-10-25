from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
			'CA106': Module('CA106', 'Web Design', 5),
			'CA115': Module('CA115', 'Digital Innovation', 5),
			'CA116': Module('CA116', 'Computer Programming I', 10),
			'CA117': Module('CA117', 'Computer Programming II', 10),
			'CA169': Module('CA169', 'Networks and Internet', 5),
			'CA170': Module('CA170', 'Operating Systems', 5),
			'CA172': Module('CA172', 'Problem Solving', 5),
			'MS121': Module('MS121', 'IT Mathematics', 10)}
	
class Student(object):

	def __init__(self, idnum, surname, firstname, mods=CA1_MODULES):
		self.__idnum = idnum
		self.__surname = surname
		self.__firstname = firstname
		self.__mods = mods
		self.__marks = {code: 0 for code in self.__mods.keys()}

	def __str__(self):
		name = '{} : {} {}'.format(self.__idnum,
									self.__firstname,
									self.__surname)
		uline = '-' * len(name)
		results =  '\n'.join([code + ' : ' + self.__mods[code].title +
							' : ' + str(self.__marks[code])
							for code in sorted(self.__mods.keys())])
		pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
		if self.passed():
			outcome = 'Pass'
		elif self.passed_by_compensation():
			outcome = 'Pass by compensation'
		else:
			outcome = 'Fail'

		return '\n'.join([name, uline, results, pm, outcome])

	def add_mark(self, module, mark):
		self.__marks[module] = mark

	def precision_mark(self):
		weighted_mark = [self.__mods[code].ects * self.__marks[code] for code in self.__mods]
		return sum(weighted_mark) / sum([self.__mods[code].ects for code in self.__mods])

	def passed(self):
		return all(self.__marks[code] >= 40 for code in self.__mods)

	def passed_by_compensation(self):
		credits_failed = sum([self.__mods[code].ects for code in self.__mods if self.__marks[code] < 40])
		return (self.precision_mark() > 45
			and all(mark >= 35 for mark in self.__marks.values())
			and credits_failed <= 10)

def main():

	s1 = Student(15334499, 'Jones', 'Zoe')
	s1.add_mark('CA103', 71)
	s1.add_mark('CA106', 65)
	s1.add_mark('CA115', 84)
	s1.add_mark('CA116', 85)
	s1.add_mark('CA117', 70)
	s1.add_mark('CA169', 68)
	s1.add_mark('CA170', 74)
	s1.add_mark('CA172', 90)
	s1.add_mark('MS121', 50)

	s2 = Student(15667755, "Brent", "Tom")
	s2.add_mark('CA103', 55)
	s2.add_mark('CA106', 35)
	s2.add_mark('CA115', 70)
	s2.add_mark('CA116', 64)
	s2.add_mark('CA117', 66)
	s2.add_mark('CA169', 50)
	s2.add_mark('CA170', 55)
	s2.add_mark('CA172', 60)
	s2.add_mark('MS121', 35)

	s3 = Student(15112277, 'Brody', 'Joe')
	s3.add_mark('CA103', 35)
	s3.add_mark('CA106', 35)
	s3.add_mark('CA115', 60)
	s3.add_mark('CA116', 60)
	s3.add_mark('CA117', 60)
	s3.add_mark('CA169', 60)
	s3.add_mark('CA170', 60)
	s3.add_mark('CA172', 60)
	s3.add_mark('MS121', 60)

	print(s1)
	print(s2)
	print(s3)
                        
if __name__ == '__main__':
	main()