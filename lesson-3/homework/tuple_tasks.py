# tuple_tasks.py

def count_occurrences(tup, element):
    return tup.count(element)

def max_element(tup):
    return max(tup)

def min_element(tup):
    return min(tup)

def check_element(tup, element):
    return element in tup

def first_element(tup):
    return tup[0] if tup else None

def last_element(tup):
    return tup[-1] if tup else None

def tuple_length(tup):
    return len(tup)

def slice_tuple(tup):
    return tup[:3]

def concatenate_tuples(tup1, tup2):
    return tup1 + tup2

def is_tuple_empty(tup):
    return len(tup) == 0

def get_all_indices_of_element(tup, element):
    return [i for i, x in enumerate(tup) if x == element]

def second_largest(tup):
    unique_sorted = sorted(set(tup), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def second_smallest(tup):
    unique_sorted = sorted(set(tup))
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def single_element_tuple(element):
    return (element,)

def list_to_tuple(lst):
    return tuple(lst)

def is_tuple_sorted(tup):
    return all(tup[i] <= tup[i + 1] for i in range(len(tup) - 1))

def max_of_subtuple(tup, start, end):
    return max(tup[start:end])

def min_of_subtuple(tup, start, end):
    return min(tup[start:end])

def remove_element_by_value(tup, element):
    lst = list(tup)
    if element in lst:
        lst.remove(element)
    return tuple(lst)

def create_nested_tuple(*args):
    return tuple(args)

def repeat_elements(tup, n):
    return tuple(x for x in tup for _ in range(n))

def create_range_tuple(start, end):
    return tuple(range(start, end + 1))

def reverse_tuple(tup):
    return tup[::-1]

def is_palindrome(tup):
    return tup == tup[::-1]

def get_unique_elements(tup):
    seen = set()
    return tuple(x for x in tup if not (x in seen or seen.add(x)))


sample_tuple = (1, 2, 3, 2, 1, 4, 5, 2, 6)

print(count_occurrences(sample_tuple, 2))
# print(max_element(sample_tuple))
# print(min_element(sample_tuple))
# print(check_element(sample_tuple, 3))
# print(first_element(sample_tuple))
# print(last_element(sample_tuple))
# print(tuple_length(sample_tuple))
# print(slice_tuple(sample_tuple))
# print(concatenate_tuples(sample_tuple, (7, 8)))
# print(is_tuple_empty(sample_tuple))
# print(get_all_indices_of_element(sample_tuple, 2))
# print(second_largest(sample_tuple))
# print(second_smallest(sample_tuple))
# print(single_element_tuple(10))
# print(list_to_tuple([1, 2, 3]))
# print(is_tuple_sorted(sample_tuple))
# print(max_of_subtuple(sample_tuple, 2, 5))
# print(min_of_subtuple(sample_tuple, 2, 5))
# print(remove_element_by_value(sample_tuple, 2))
# print(create_nested_tuple((1, 2), (3, 4)))
# print(repeat_elements(sample_tuple, 2))
# print(create_range_tuple(1, 10))
# print(reverse_tuple(sample_tuple))
# print(is_palindrome(sample_tuple))
# print(get_unique_elements(sample_tuple))