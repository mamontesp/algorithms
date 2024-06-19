"""Write a function that takes a list of names and returns the names sorted
    by the number of vowels in each name in descending order. If two names have 
    the same number of vowels, sort them alphabetically. 
"""
from typing import List, Tuple
import re
import argparse

def get_vowels_number(name: str) -> Tuple[int, str]:
    """Get the number of vowels in a string

    Args:
        name (str): word

    Returns:
        int: Number of vowels
        str: name
    """
    pattern = r'[aeiouAEIOU]'
    vowels = list(re.findall(pattern, name))
    print(f'vowels {vowels}')
    return (6 - len(vowels), name)

def sort_vowels(names: List) -> List[str]:
    """Sorts a list by the number of vowels, If two names have 
    the same number of vowels, sort them alphabetically. 

    Args:
        names (List): List of names to sort

    Returns:
        List[str]: Sorted list
    """
    names.sort(key = get_vowels_number)
    return names

def test():
    """Test function for sort_vowels method
    """
    example_list = ["Goku", "Vegeta", "Piccolo", "Gohan"]
    expected_sorted_list =  ["Piccolo", "Vegeta", "Gohan", "Goku"]

    sorted_list = sort_vowels(example_list)
    print (f'sorted_list {sorted_list}')
    assert expected_sorted_list == sorted_list 

def main():
    """Gets a list of names and returns it sorted by the number of vowels in each name in descending order
    """
    parser = argparse.ArgumentParser(description="Sort a list by the number of vowels in each name in descending order")
    parser.add_argument('names', nargs='+', type=str, help="List of names")
    args = parser.parse_args()

    input_names = args.names
    sorted_list = sort_vowels(input_names)
    print (f'sorted_list {sorted_list}')

if __name__ == '__main__':
    main()