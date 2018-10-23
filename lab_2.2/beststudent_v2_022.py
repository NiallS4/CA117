import sys

def main():
	try:
		largest = 0
		file = sys.argv[1]
		with open(file, 'r') as f:
			students = f.readlines()
			for line in students:
				line = line.strip()
				tokens = line.split()
				tokens[1:] = [' '.join(tokens[1:])]
				if int(tokens[0]) > largest:
					largest = int(tokens[0])
					name = tokens[1]
			print('Best student: {}'.format(name))
			print('Best mark: {}'.format(largest))
	except FileNotFoundError:
		print('The file {} could not be opened.'.format(file))
	except ValueError:
		print('Invalid mark {} encountered. Exiting.'.format(tokens[0]))

if __name__ == '__main__':
	main()