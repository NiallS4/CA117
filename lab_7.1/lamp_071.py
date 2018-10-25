class Lamp(object):

	def __init__(self, on=False):
		self.on = on

	def toggle(self):
		self.on = not self.on

	def turn_on(self):
		if self.on == False:
			self.on = True

	def turn_off(self):
		if self.on == True:
			self.on = False