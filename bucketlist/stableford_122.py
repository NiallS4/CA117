import sys

par1 = sys.stdin.readline()
par = [int(p) for p in par1.strip().split()]
index1 = sys.stdin.readline()
index = [int(i) for i in index1.strip().split()]

hole_index = {}
for hole in range(0, 18):
	hole_index[hole] = index[hole] - 1

score_to_par = {-7:9, -6:8, -5:7, -4:6, -3:5, -2:4, -1:3, 0:2, 1:1, 2:0}

def main():
	output = {}
	disq = []
	longest_len = 0
	for line in sys.stdin:
		line = line.strip()
		names = ' '.join(line.split()[:-19])
		if longest_len < len(names):
			longest_len = len(names)
		player_hc = int(line.split()[-19])
		strokes = line.split()[-18:]
		player_points = score_calculator(player_hc, strokes)
		
		if player_points =='Disqualified':
			disq.append(names)
		else:
			if player_points in output:
				output[player_points].append(names)
			else:
				output[player_points] = names

	q = list(output)
	q.sort(reverse=True)
	for p in q:
		name = output[p]
		print('{:>{}s} : {:>2d}'.format(name, longest_len, p))
	for p in disq:
		print('{:>{}s} : Disqualified'.format(p, longest_len))
	
def total_handicap(hc, hole):
	index = hole_index[hole]
	if index < hc % 18:
		handicap = (hc // 18) + 1
	else:
		handicap = (hc // 18)
	return handicap
	
def score_calculator(hc, strokes):
	total = 0
	for i in range(0, 18):
		if 'X' not in strokes[i]:
			try:
				stroke = int(strokes[i])
			except:
				return 'Disqualified'
			net_strokes = int(strokes[i]) - total_handicap(hc, i)
			result = net_strokes - par[i]
			score = 0
			if result < 2:
				score = score_to_par[result]
			total = total + score
	return total
	
if __name__ == '__main__':
	main()