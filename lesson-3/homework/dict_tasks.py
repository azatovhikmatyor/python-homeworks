# dictionary_tasks.py

def get_value(d, key):
    return d.get(key)

def check_key(d, key):
    return key in d

def count_keys(d):
    return len(d)

def get_all_keys(d):
    return list(d.keys())

def get_all_values(d):
    return list(d.values())

def merge_dictionaries(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

def remove_key(d, key):
    d.pop(key, None)
    return d

def clear_dictionary():
    return {}

def is_dictionary_empty(d):
    return len(d) == 0

def get_key_value_pair(d, key):
    return (key, d[key]) if key in d else None

def update_value(d, key, value):
    d[key] = value
    return d

def count_value_occurrences(d, value):
    return list(d.values()).count(value)

def invert_dictionary(d):
    return {v: k for k, v in d.items()}

def find_keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]

def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

def check_for_nested_dictionaries(d):
    return any(isinstance(v, dict) for v in d.values())

def get_nested_value(d, outer_key, inner_key):
    return d.get(outer_key, {}).get(inner_key)

def create_default_dictionary(default_value):
    from collections import defaultdict
    return defaultdict(lambda: default_value)

def count_unique_values(d):
    return len(set(d.values()))

def sort_dictionary_by_key(d):
    return dict(sorted(d.items()))

def sort_dictionary_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def filter_by_value(d, condition):
    return {k: v for k, v in d.items() if condition(v)}

def check_for_common_keys(d1, d2):
    return bool(set(d1.keys()) & set(d2.keys()))

def create_dict_from_tuple(tuples):
    return dict(tuples)

def get_first_key_value_pair(d):
    return next(iter(d.items()), None)


sample_dict = {'a': 1, 'b': 2, 'c': 3}
sample_dict2 = {'c': 4, 'd': 5}
sample_tuple = (('x', 10), ('y', 20), ('z', 30))

print(get_value(sample_dict, 'a'))
# print(check_key(sample_dict, 'b'))
# print(count_keys(sample_dict))
# print(get_all_keys(sample_dict))
# print(get_all_values(sample_dict))
# print(merge_dictionaries(sample_dict, sample_dict2))
# print(remove_key(sample_dict.copy(), 'b'))
# print(clear_dictionary())
# print(is_dictionary_empty(sample_dict))
# print(get_key_value_pair(sample_dict, 'c'))
# print(update_value(sample_dict.copy(), 'a', 10))
# print(count_value_occurrences(sample_dict, 2))
# print(invert_dictionary(sample_dict))
# print(find_keys_with_value(sample_dict, 3))
# print(create_dict_from_lists(['a', 'b', 'c'], [1, 2, 3]))
# print(check_for_nested_dictionaries({'a': {'nested': 1}, 'b': 2}))
# print(get_nested_value({'a': {'nested': 1}}, 'a', 'nested'))
# print(create_default_dictionary(0)['missing_key'])
# print(count_unique_values(sample_dict))
# print(sort_dictionary_by_key(sample_dict))
# print(sort_dictionary_by_value(sample_dict))
# print(filter_by_value(sample_dict, lambda x: x > 1))
# print(check_for_common_keys(sample_dict, sample_dict2))
# print(create_dict_from_tuple(sample_tuple))
# print(get_first_key_value_pair(sample_dict))