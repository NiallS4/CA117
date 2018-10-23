def l2d(s):
	d = {}
	line1 = s.readline().strip()
	line2 = s.readline().strip()
	key, value = line1.split(), line2.split()
		
	for i in range(len(key)):
		d[key[i]] = value[i]
	
	return d