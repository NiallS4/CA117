class Customer(object):

	discount = 0

	def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
		self.name = name
		self.balance = balance
		self.addr_line1 = addr_line1
		self.addr_line2 = addr_line2
		self.addr_line3 = addr_line3

	def owes(self):
		return self.balance * (1 - self.discount)

	def __str__(self):
		l = []
		l.append(self.name)
		l.append(self.addr_line1)
		l.append(self.addr_line2)
		l.append(self.addr_line3)
		l.append('Balance: {:.2f}'.format(self.balance))
		l.append('Discount: {}%'.format(int(self.discount*100)))
		l.append('Amount due: {:.2f}'.format(self.owes()))
		return '\n'.join(l)

class ValuedCustomer(Customer):

	discount = 0.1

def main():

	c1 = Customer('Jimmy', 100, '22 Main Street', 'Naas', 'Kildare');
	c2 = ValuedCustomer('Lucy', 100, '23 Main Street', 'Roosky', 'Roscommon');
	c3 = Customer('Fred', 200, '24 Main Street', 'Sneem', 'Kerry');

	print(c1)
	print(c2)
	print(c3)

if __name__ == '__main__':
	main()