import sys

def mins2secs(t):
	mins, secs = t.split(':')
	seconds = int(mins) * 60 + int(secs)
	return seconds

def main():
	d = {}
	for line in sys.stdin:
		try:
			tokens = line.strip().split()
			names, times = tokens[0], tokens[1:]
			d[names] = min(times, key=mins2secs)
		except ValueError:
			continue
	
	winner = min(d.items(), key=lambda x: mins2secs(x[1]))
	print('{} : {}'.format(winner[0], winner[1]))
		
if __name__ == '__main__':
	main()