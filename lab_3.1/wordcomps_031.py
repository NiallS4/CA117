import sys

s = [line.strip() for line in sys.stdin]

def len17(words):
	return [w for w in words if len(w) == 17]

def len18plus(words):
	return [w for w in words if len(w) >= 18]

def extractwords(words):
	return min([w for w in words if allvowels(w.lower())], key=len)

def allvowels(w):
	return 'a' in w and 'e' in w and 'i' in w and 'o' in w and 'u' in w

def four_a(words):
	acount = [w.lower().count('a') for w in words]
	foura = [w for w in words if w.lower().count('a') == 4]
	return foura

def twoplus_q(words):
	qcount = [w.lower().count('q') for w in words]
	twoplusq = [w for w in words if w.lower().count('q') >= 2]
	return twoplusq

def cie(words):
	return [w for w in words if 'cie' in w.lower()]
		
def angle(words):
	return [w for w in words if ('a' in w.lower() and 'n' in w.lower() and 'g' in w.lower() and 'l' in w.lower() and 'e' in w.lower()) and len(w) == 5  and w.lower() != 'angle']

def _iary(words):
	return len([w for w in words if w.lower()[-4:] == 'iary'])
	
def q_not_u(words):
	return [w for w in words if 'q' in w.lower() and 'qu' not in w.lower()]
	
def most_es(words):
	ecount = [w.lower().count('e') for w in words]
	emax = max(ecount)
	mostes = [w for w in words if w.lower().count('e') == emax]
	return mostes

def main():
	print("Words containing 17 letters: {}".format(len17(s)))
	print("Words containing 18+ letters: {}".format(len18plus(s)))
	print("Shortest word containing all vowels: {}".format(extractwords(s)))
	print("Words with 4 a's: {}".format(four_a(s)))
	print("Words with 2+ q's: {}".format(twoplus_q(s)))
	print("Words containing cie: {}".format(cie(s)))
	print("Anagrams of angle: {}".format(angle(s)))
	print("Words ending in iary: {}".format(_iary(s)))
	print("Words with q but no u: {}".format(q_not_u(s)))
	print("Words with most e's: {}".format(most_es(s)))

if __name__ == '__main__':
	main()