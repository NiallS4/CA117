import sys
import string

def build_dictionary():
	d = {}
	for line in sys.stdin:
		words = line.lower().strip().split()
		for word in words:
			word = word.strip(string.punctuation)
			if word == '':
				continue
			if word not in d:
				d[word] = 1
			else:
				d[word] += 1
	return d

def main():
	d = build_dictionary()
	nd = {}
	for k, v in d.items():
		if len(k) > 3 and v >= 3:
			nd[k] = v
	for k,v in sorted(nd.items()):
		width_keys = len(max(nd.keys(), key=len))
		width_values = len(max(nd.items()))
		print('{:>{:d}s} : {:>{:d}d}'.format(k, width_keys, v, width_values))

if __name__ == '__main__':
	main()
