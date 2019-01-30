import sys

def main():
	try:
		highest = 0
		file = sys.argv[1]
		with open(file, 'r') as f:
			students = f.readlines()
			for line in students:
				try:
					tokens = line.strip().split()
					tokens[1:] = [' '.join(tokens[1:])]
					mark = int(tokens[0])
					if mark > highest:
						highest = mark
						name = tokens[1]
				except ValueError:
					print('Invalid mark {} encountered. Skipping.'.format(tokens[0]))
			
			print('Best student: {}'.format(name))
			print('Best mark: {}'.format(highest))
	
	except FileNotFoundError:
		print('The file {} could not be opened.'.format(file))

if __name__ == '__main__':
	main()