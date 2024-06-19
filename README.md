# Algorithms Playground for Andrea :heart:



## Installation

```bash
source env/bin/activate
```

## Usage

### For max product cassidoo_newsletter/2024/05:

- Description: Write a function that takes in a list (of length >= 3) of numbers, and returns the maximum product that can be obtained by multiplying any three integers from the list

- Example: 
```bash
maxProduct([2, 4, 1, 3, -5, 6])
72 (4*3*6)
```

Solution: 
```bash
cd cassidoo_newsletter/2024/05
python max_product 1 2 3 5 6 3
```

#### Author's notes
The approach to this problem depends on the situation. To make this interesting, let's think in a large list and a variable number of integers that need to be multiplied:

- Sorted list gives time complexity of O(1), only the three first numbers and the two last need to be accessed. But what if this list changes frequently, every write to the sorted list is O(n)
- Heap gives time complexity of O(n), as there are a number of mins to find, each search requires a new heapify process.

### For sort by number of vowels cassidoo_newsletter/2024/06:
- Description: Write a function that takes a list of names and returns the names sorted by the number of vowels in each name in descending order. If two names have the same number of vowels, sort them alphabetically. 

- Example: 
```python
example_list = ["Goku", "Vegeta", "Piccolo", "Gohan"]
sorted_list = sort_vowels(example_list)
expected_sorted_list =  ["Piccolo", "Vegeta", "Gohan", "Goku"]
assert expected_sorted_list == sorted_list 
```

Solution: 
```bash
cd cassidoo_newsletter/2024/06
python sort_vowels_number.py Andrea Oscar Emilia Cassidy
```

Returns:
``` bash
['Emilia', 'Andrea', 'Cassidy', 'Oscar']
```



## License

[MIT](https://choosealicense.com/licenses/mit/)