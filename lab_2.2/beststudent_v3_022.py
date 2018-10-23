import sys

def main():
	try:
		largest = 0
		file = sys.argv[1]
		with open(file, 'r') as f:
			students = f.readlines()
			for line in students:
				try:
					line = line.strip()
					tokens = line.split()
					tokens[1:] = [' '.join(tokens[1:])]
					mark = int(tokens[0])
					if mark > largest:
						largest = mark
						name = tokens[1]
				except ValueError:
					print('Invalid mark {} encountered. Skipping.'.format(tokens[0]))
			print('Best student: {}'.format(name))
			print('Best mark: {}'.format(largest))
	except FileNotFoundError:
		print('The file {} could not be opened.'.format(file))

if __name__ == '__main__':
	main()