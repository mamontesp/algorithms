import datetime
import sys


def quicksort(arr):
	if len(arr)<= 1:
		return arr
	pivot = arr[0]
	left  = [x for x in arr[1:] if x > pivot]
	right = [x for x in arr[1:] if x <= pivot]
	return quicksort(left) + [pivot] + quicksort(right)

def get_longest_time_gap(arr: []):
	longest_time_gap = 0
	if len(arr)<=1:
		return 0
	arr_diff = []
	for i in range(len(arr) - 1):
		diff = datetime.datetime.strptime(arr[i], '%H:%M') - datetime.datetime.strptime(arr[i+1], '%H:%M')
		diff_minutes = int(abs(diff.total_seconds() / 60))
		arr_diff.append(diff_minutes)
	print(arr_diff)
	return quicksort(arr_diff)[0]

def test_get_longest_time_gap():
	array_input = ['09:00', '10:00']
	expected_output = 60
	output = get_longest_time_gap(array_input)
	assert expected_output == output

if __name__ == '__main__':
	#test_get_longest_time_gap()
	input_array = [x for x in sys.argv[1].replace(' ', '').split(',')]
	print(f'input_array {input_array}')
	print(f'{get_longest_time_gap(input_array)}')





