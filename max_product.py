## Write a function that takes in a list (of length >= 3) of numbers, 
## and returns the maximum product that can be obtained by multiplying 
## any three integers from the list

## maxProduct([2, 4, 1, 3, -5, 6])
## 72 (4*3*6)

from typing import List

def heapify(input_list: List, length: int, i: int):
	print('heap')
	largest = i
	left_tree_index =  2 * i + 1
	right_tree_index =  2 * i + 2

	if left_tree_index < length and input_list[largest] < input_list[left_tree_index]:
		#mark left as the largest
		largest = left_tree_index

	if right_tree_index < length and input_list[largest] < input_list[right_tree_index]:
		#mark right as the largest
		largest = right_tree_index

	## what if largest has changed?
	if largest != i:
		#reassign
		input_list[i], input_list[largest] = input_list[largest], input_list[i]
		#Heapify only the affected sub-tree
		heapify(input_list, length, largest)


def get_max_product(heap, multiples: int = 3) -> int:
	product = 1
	for i in range(multiples):
		product *= heap[0]
		heap[0] = -1000
		heapify(heap, len(heap), 0)
	return product


if __name__ == '__main__':
	input_list = [2, 4, 1, 3, -5, 6]
	length = len(input_list)
	for i in range(length//2 - 1, -1, -1):
		heapify(input_list, length, i)

	max_product = get_max_product(input_list)
	expected_max_product = 72

	if max_product == expected_max_product:
		print(f'Well done {max_product}')
	else:
		print(f'Keep trying {max_product}')
	##testing
	"""
	expected_heap = [6, 4, 2, 3, -5, 1]
	if input_list == expected_heap:
		print(True)
	else:
		print(False)
	"""

