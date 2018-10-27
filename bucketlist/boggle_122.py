import sys

def load_boards(filename):
	global boards
	with open(filename) as f:
		lines = [l.strip() for l in f]
		boards += [[l[i:i + 4] for i in range(0, 13, 4)] for l in lines]

def load_dictionary(filename):
	global dict_words
	with open(filename) as f:
		dict_words = [l.strip().lower() for l in f]

def find(word, found=False):

	low = 0
	high = len(dict_words) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = dict_words[mid] if found else dict_words[mid][:len(word)]

		if guess > word:
			high = mid - 1
		elif guess < word:
			low = mid + 1
		else:
			# print(word)
			return True
	return False

points = {
		1: 0,
		2: 0,
		3: 1,
		4: 1,
		5: 2,
		6: 3,
		7: 5
		}

cardinals = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2) if not i == j == 0)
dict_words = []
boards = []

def get_next_words(board, pos=(0, 0)):
	cur = pos[-1]
	next_pos = set(c_tuple(add_tuple(cur, offset)) for offset in cardinals)
	next_pos = set(p for p in next_pos if p not in pos)
	next_words = {pos + (p,): build_word(board, pos + (p,)) for p in next_pos}
	return next_words

def find_all_substrings(board, start_pos):
	w = get_next_words(board, start_pos)
	w = {k:v for (k, v) in w.items() if find(v)}
	if w:
		nw = dict(w)
		for pos in w:
			nw.update(find_all_substrings(board, pos))
		return nw
	else:
		return {}

def find_all_words(board):
	start_positions = tuple((i, j) for i in range(0, 4) for j in range(0, 4))
	subs = {}
	for pos in start_positions:
		subs.update(find_all_substrings(board, (pos,)))
	words = set(s for s in subs.values() if find(s, True))
	return sorted(words)

def add_tuple(t1, t2):
	return (t1[0] + t2[0], t1[1] + t2[1])

def c_tuple(t, c_min=0, c_max=3):
	return tuple(max(c_min, min(c_max, x)) for x in t)

def build_word(board, pos):
	return ''.join(board[p[1]][p[0]] for p in pos)

def main():
	load_boards(sys.argv[1])
	load_dictionary(sys.argv[2])

	for c in boards:
		words = find_all_words(c)
		total_points = sum(points.get(len(w), 11) for w in words)
		print('Possible points: {}'.format(total_points))

if __name__ == '__main__':
	main()