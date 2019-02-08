import sys

def main():
	d = {}
	excl = []
	for line in sys.stdin:
		line = line.strip().split(':')
		name, marks =  line[0], line[1].split(',')
		try:
			total = 0
			for num in marks:
				total += int(num)
			d[name] = total
		except ValueError:
			excl.append(name)
	
	for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
		print('{} : {}'.format(k, v))
	print('Skipped:')
	for name in excl:
		print(name)
	
if __name__ == '__main__':
	main()