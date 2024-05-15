## Write a function that takes in a list (of length >= 3) of numbers, 
## and returns the maximum product that can be obtained by multiplying 
## any three integers from the list

## maxProduct([2, 4, 1, 3, -5, 6])
## 72 (4*3*6)

from typing import List
import argparse

def min_heapify(input_list: List, length: int, i: int):
	smallest = i
	left_tree_index = 2 * i + 1
	right_tree_index = 2 * i + 2

	#verify left tree
	if left_tree_index < length and input_list[smallest] > input_list[left_tree_index]:
		smallest = left_tree_index

	#verify right tree
	if right_tree_index < length and input_list[smallest] > input_list[right_tree_index]:
		smallest = right_tree_index

	# if smallest changed
	if smallest != i:
		input_list[i], input_list[smallest] = input_list[smallest], input_list[i]
		min_heapify(input_list, length, smallest)

def max_heapify(input_list: List, length: int, i: int):
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
		max_heapify(input_list, length, largest)

def get_max_product(heap, multiples: int = 3) -> int:
	product = 1
	for i in range(multiples):
		product *= heap[0]
		heap[0] = float('-inf')
		max_heapify(heap, len(heap), 0)
	return product

def get_max_product_min_heap(heap, max_number, multiples: int = 3) -> int:
	product = max_number
	for i in range(multiples - 1 ):
		product*= heap[0]
		heap[0] = float('inf')
		min_heapify(heap, len(heap), 0)
	return product

def main():
    parser = argparse.ArgumentParser(description="Find the maximum product of any three integers from a list")
    parser.add_argument('nums', nargs='+', type=int, help="List of integers")
    args = parser.parse_args()

    input_list_positive = args.nums
    input_list_negative = input_list_positive[::]
    length = len(input_list_positive)

    if length < 3:
    	raise Exception("This script only works for list with more than three elements")

    for i in range(length//2 - 1, -1, -1):
    	max_heapify(input_list_positive, length, i)
    	min_heapify(input_list_negative, length, i)

    max_number = input_list_positive[0]

    print(f'max_heapify {input_list_positive} min_heapify {input_list_negative}')
    result = max(get_max_product(input_list_positive), get_max_product_min_heap(input_list_negative, max_number))
    print(f"The maximum product of any three integers in the list is: {result}")


if __name__ == '__main__':
	main()

