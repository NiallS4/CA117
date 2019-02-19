import sys
import string

def build_dictionary():
	d = {}
	for line in sys.stdin:
		line = line.lower().strip()
		for c in line:
			c = c.strip(string.punctuation)
			if c == '':
				continue
			if c not in d:
				d[c] = 1
			else:
				d[c] += 1
	return d

def main():
	d = build_dictionary()
	nd = {}
	vowels = 'aeiou'
	for k, v in d.items():
		if k in vowels:
			nd[k] = v
	for k, v in sorted(nd.items(), key=lambda x: x[1], reverse=True):
		width_keys = len(max(nd.keys()))
		width_values = len(str(max(nd.values())))
		print('{:>{:d}s} : {:{:d}d}'.format(k, width_keys, v, width_values))
	

if __name__ == '__main__':
	main()
