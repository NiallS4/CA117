import sys
import calendar

day, month, year = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

def main():
	if calendar.weekday(year, month, day) == 0:
		print("You were born on a Monday and Monday's child is fair of face.")
	if calendar.weekday(year, month, day) == 1:
		print("You were born on a Tuesday and Tuesday's child is full of grace.")
	if calendar.weekday(year, month, day) == 2:
		print("You were born on a Wednesday and Wednesday's child is full of woe.")
	if calendar.weekday(year, month, day) == 3:
		print("You were born on a Thursday and Thursday's child has far to go.")
	if calendar.weekday(year, month, day) == 4:
		print("You were born on a Friday and Friday's child is loving and giving.")
	if calendar.weekday(year, month, day) == 5:
		print("You were born on a Saturday and Saturday's child works hard for a living.")
	if calendar.weekday(year, month, day) == 6:
		print("You were born on a Sunday and Sunday's child is fair and wise and good in every way.")

if __name__ == '__main__':
	main()