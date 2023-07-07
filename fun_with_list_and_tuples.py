# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def sort_list(sample_list):
    sorted_list = sorted(sample_list, key=last_element)
    return sorted_list

def last_element(tuple):
    return tuple[-1]


sorted_list = sort_list(sample_list)
print(sorted_list)
