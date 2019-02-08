import sys

def build_dictionary(filename):
	d = {}
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip().split()
			food, calories = ' '.join(line[:-1]), line[-1]
			d[food] = calories
	return d

def main():
		d = build_dictionary(sys.argv[1])
		nd = {}
		for line in sys.stdin:
			l = []
			line = line.strip().split(',')
			name, foods = line[0], line[1:]
			for food in foods:
				if food in d:
					food = d[food]
					l.append(int(food))
				else:
					n = 100
					l.append(n)
			nd[name] = sum(l)

		for k, v in sorted(nd.items(), key=lambda x: x[1]):
			width_keys = len(max(nd.keys(), key=len))
			width_values = len(str(max(nd.values())))
			print('{:>{:d}s} : {:{:d}d}'.format(k, width_keys, v, width_values))

if __name__ == '__main__':
	main()