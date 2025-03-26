# Write a function that finds the longest streak of consecutive true values 
# in a boolean array that meets or exceeds a given streak goal. 
# Return 0 if no such streak exists. 

# findLongestStreak([true, true, false, true, true, true], 3) 3
import argparse
import sys

def find_longest_streak(arr: [], wanted_streak: int ):
	streak = 0
	longest_streak = 0

	for i in arr:
		print(f"find_l {i}")
		if i:
			streak +=1 
		else:
			if longest_streak < streak:
				longest_streak = streak
				streak = 0

	if longest_streak < streak:
		longest_streak = streak
	print(f'longest_streak {longest_streak}')
	if longest_streak >= wanted_streak:
		return longest_streak
	else:
		return 0	

def test_find_longest_streak():
	test_array= [True, True, False, False]
	wanted_streak = 2
	expected_longest_streak = 2
	longest_streak = find_longest_streak(test_array, wanted_streak)
	assert longest_streak == expected_longest_streak
	print(f"longest streak {longest_streak}")


if __name__ == '__main__':
	#test_find_longest_streak()
	array = [bool(i.lower().replace(' ', '')=='true') for i in sys.argv[1].split(',')]

	print (f"input array {array}")
	wanted_streak = int(sys.argv[2])
	longest_streak = find_longest_streak(array, wanted_streak)
	print (longest_streak)
	



