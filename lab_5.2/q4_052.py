import sys

def build_dictionary(filename):
	d = {}
	with open(sys.argv[1], 'r') as f:
		for line in f:
			line = line.strip()
			food = line.split()[:-1]
			food = ' '.join(food)
			calories = line.split()[-1]
			d[food] = calories
	return d

def main():
		d = build_dictionary(sys.argv[1])
		nd = {}
		for line in sys.stdin:
			l = []
			line = line.strip().split(',')
			name, foods = line[0], line[1:]
			for f in foods:
				if f in d:
					f = d[f]
					l.append(int(f))
				else:
					n = 100
					l.append(n)
			totals = sum(l)
			nd[name] = totals

		for k, v in sorted(nd.items(), key=lambda x: x[1]):
			width_keys = len(max(nd.keys(), key=len))
			width_values = len(str(max(nd.values())))
			print('{:>{:d}s} : {:{:d}d}'.format(k, width_keys, v, width_values))

if __name__ == '__main__':
	main()