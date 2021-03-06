import sys

def q_not_u(words):
	for w in words:
		return [w for w in words if w.lower().count('q') > w.lower().count('qu')]
	

def main():
	words = []
	for line in sys.stdin:
		words.append(line.strip())
	print('Words with q but no u: {}'.format(q_not_u(words)))

if __name__ == '__main__':
	main()

# Extended list of test cases:
# question
# QUESTION
# Colloq
# IQ
# Iraq
# Iraqi
# IRAQ
# IRAQI
# q
# Qatar
# QED
# q's
# seq
# inquest
# qequ
# aqu
# QEQU
# AQU
