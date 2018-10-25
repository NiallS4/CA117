class Student(object):

	def __init__(self, surname, forename, sid, modlist=None):
		if modlist is None:
			modlist = []
		self.surname = surname
		self.forename = forename
		self.sid = sid
		self.modlist = modlist

	def add_module(self, m):
		self.modlist.append(m)

	def del_module(self, m):
		try:
			self.modlist.remove(m)
		except:
			pass

	def print_details(self):
		print('ID: {}'.format(self.sid))
		print('Surname: {}'.format(self.surname))
		print('Forename: {}'.format(self.forename))
		print('Modules: {}'.format(' '.join(self.modlist)))