import sys

def main():
	file = sys.argv[1]
	with open(file, 'r') as f:
		students = f.readlines()
		highest = 0
		for line in students:
			line = line.strip()
			tokens = line.split()
			tokens[1:] = [' '.join(tokens[1:])]
			mark = int(tokens[0])
			name = tokens[1]
			if mark > highest:
				highest = mark
				names = [name]
			elif mark == highest:
				names.append(name)

		print('Best student(s): {}'.format(', '.join(names)))
		print('Best mark: {}'.format(highest))

if __name__ == '__main__':
	main()