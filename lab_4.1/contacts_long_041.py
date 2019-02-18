import sys

def build_dictionary(file):
	d = {}
	with open(file, 'r') as f:
		for line in f:
			name, phone, email = line.strip().split()
			d[name] = phone, email
	return d

def main():
	d = build_dictionary(sys.argv[1])
	for line in sys.stdin:
		name = line.strip()
		print('Name: {}'.format(name))
		try:
			print('Phone: {}'.format(d[name][0]))
			print('Email: {}'.format(d[name][1]))
		except KeyError:
			print('No such contact')

if __name__ == '__main__':
	main()