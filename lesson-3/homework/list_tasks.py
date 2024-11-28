# List Tasks

def count_occurrences(lst, element):
    return lst.count(element)

def sum_of_elements(lst):
    return sum(lst)

def max_element(lst):
    return max(lst) if lst else None

def min_element(lst):
    return min(lst) if lst else None

def check_element(lst, element):
    return element in lst

def first_element(lst):
    return lst[0] if lst else None

def last_element(lst):
    return lst[-1] if lst else None

def slice_list(lst):
    return lst[:3]

def reverse_list(lst):
    return lst[::-1]

def sort_list(lst):
    return sorted(lst)

def remove_duplicates(lst):
    return list(set(lst))

def insert_element(lst, element, index):
    lst.insert(index, element)
    return lst

def index_of_element(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return None

def check_for_empty_list(lst):
    return len(lst) == 0

def count_even_numbers(lst):
    return len([num for num in lst if num % 2 == 0])

def count_odd_numbers(lst):
    return len([num for num in lst if num % 2 != 0])

def concatenate_lists(lst1, lst2):
    return lst1 + lst2

def find_sublist(lst, sublist):
    sublist_len = len(sublist)
    return any(lst[i:i + sublist_len] == sublist for i in range(len(lst) - sublist_len + 1))

def replace_element(lst, old, new):
    try:
        idx = lst.index(old)
        lst[idx] = new
    except ValueError:
        pass
    return lst

def find_second_largest(lst):
    unique_elements = list(set(lst))
    unique_elements.sort()
    return unique_elements[-2] if len(unique_elements) > 1 else None

def find_second_smallest(lst):
    unique_elements = list(set(lst))
    unique_elements.sort()
    return unique_elements[1] if len(unique_elements) > 1 else None

def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def filter_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]

def list_length(lst):
    return len(lst)

def create_copy(lst):
    return lst[:]

def get_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None
    if n % 2 == 1:
        return lst[n // 2]
    return lst[n // 2 - 1: n // 2 + 1]

def find_maximum_of_sublist(lst, start, end):
    return max(lst[start:end+1])

def find_minimum_of_sublist(lst, start, end):
    return min(lst[start:end+1])

def remove_element_by_index(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    return lst

def check_if_list_is_sorted(lst):
    return lst == sorted(lst)

def repeat_elements(lst, times):
    return [item for item in lst for _ in range(times)]

def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)

def find_all_indices(lst, element):
    return [i for i, e in enumerate(lst) if e == element]

def rotate_list(lst, shift):
    shift %= len(lst)
    return lst[-shift:] + lst[:-shift]

def create_range_list(start, end):
    return list(range(start, end + 1))

def sum_of_positive_numbers(lst):
    return sum(num for num in lst if num > 0)

def sum_of_negative_numbers(lst):
    return sum(num for num in lst if num < 0)

def check_palindrome(lst):
    return lst == lst[::-1]

def create_nested_list(lst, sublist_size):
    return [lst[i:i + sublist_size] for i in range(0, len(lst), sublist_size)]

def get_unique_elements_in_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Testing each function by calling them with sample inputs

sample_list = [1, 2, 3, 4, 5, 3, 3, 2]
print(count_occurrences(sample_list, 3))
# print(sum_of_elements(sample_list))
# print(max_element(sample_list))
# print(min_element(sample_list))
# print(check_element(sample_list, 3))
# print(first_element(sample_list))
# print(last_element(sample_list))
# print(slice_list(sample_list))
# print(reverse_list(sample_list))
# print(sort_list(sample_list))
# print(remove_duplicates(sample_list))
# print(insert_element(sample_list[:], 6, 2))
# print(index_of_element(sample_list, 3))
# print(check_for_empty_list(sample_list))
# print(count_even_numbers(sample_list))
# print(count_odd_numbers(sample_list))
# print(concatenate_lists(sample_list, [6, 7, 8]))
# print(find_sublist(sample_list, [3, 4]))
# print(replace_element(sample_list[:], 3, 9))
# print(find_second_largest(sample_list))
# print(find_second_smallest(sample_list))
# print(filter_even_numbers(sample_list))
# print(filter_odd_numbers(sample_list))
# print(list_length(sample_list))
# print(create_copy(sample_list))
# print(get_middle_element(sample_list))
# print(find_maximum_of_sublist(sample_list, 1, 4))
# print(find_minimum_of_sublist(sample_list, 1, 4))
# print(remove_element_by_index(sample_list[:], 2))
# print(check_if_list_is_sorted(sample_list))
# print(repeat_elements(sample_list, 2))
# print(merge_and_sort(sample_list, [6, 7, 8]))
# print(find_all_indices(sample_list, 3))
# print(rotate_list(sample_list, 2))
# print(create_range_list(1, 5))
# print(sum_of_positive_numbers([-1, 2, 3, -4, 5]))
# print(sum_of_negative_numbers([-1, 2, 3, -4, 5]))
# print(check_palindrome([1, 2, 3, 2, 1]))
# print(create_nested_list(sample_list, 2))
# print(get_unique_elements_in_order([1, 2, 3, 3, 4, 2, 5]))