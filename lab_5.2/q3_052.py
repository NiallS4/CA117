def build_dictionary(filename):
	d = {}
	with open(filename, 'r') as f:
		for line in f:
			animal, number = line.split()
			d[animal] = int(number)
	return d

def extract_range(d, low, high):
	d = {k:v for k, v in d.items() if v >= low and v <= high}
	return d