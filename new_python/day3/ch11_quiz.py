#1.
def find_dups(L):
    """ (list) -> set
    Return the number of duplicates numbers from L.
    >>> find_dups([1, 1, 2, 3, 4, 2])
    {1, 2}
    >>> find_dups([1, 2, 3, 4])
    set()
    """
    elem_set = set()
    dups_set = set()
    for entry in L:
        len_initial = len(elem_set)
        elem_set.add(entry)
        len_after = len(elem_set)
        if len_initial == len_after:
            dups_set.add(entry)
    return(dups_set)

#5.
def least_likely(particle_to_probability):
    """ (dict of {str: float}) -> str
    Return the particle from particle_to_probability with the lowest
    probablity.
    >>> least_likely({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon':
    0.07})
    'meson'
    """
    smallest = 1
    name = ''
    for particle in particle_to_probability:
        probability = particle_to_probability[particle]
        if probability < smallest:
            smallest = probability
            name = particle
    return particle

#6.
def count_duplicates(dictionary):
    """ (dic) -> int
    Return the number of duplicate values in dictionary.
    >>> count_duplicates({'R': 1, 'G': 2, 'B': 2, 'Y': 1, 'P': 3})
    2
    """
    duplicates = 0
    values = list(dictionary.values())
    for item in values:
        # if an item appears at least 2 times, it is a duplicate
        if values.count(item) >= 2:
            duplicates = duplicates + 1
            # remove that item from the list
            num_occurrences = values.count(item)
            for i in range(num_occurrences):
                values.remove(item)
    return duplicates

#9.
def db_headings(dict_of_dict):
    """ (dict of dict) -> set
    Return a set of the keys in the inner dictionaries in dict_of_dict.
    >>> db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    {1, 2, 3}
    """
    inner_keys = set()
    for key in dict_of_dict:
        for inner_key in dict_of_dict[key]:
            inner_keys.add(inner_key)
    return inner_keys

#10.
def db_consistent(dict_of_dict):
    """ (dict of dict) -> set
    Return whether all inner dictionaries in dict_of_dict contain the same
    keys.
    >>> db_consistent({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    False
    >>> db_consistent({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 1: 'd'}})
    True
    """
    inner_keys_list = []
    # Build a list of list of keys
    for key in dict_of_dict:
        inner_keys = list(dict_of_dict[key].keys())
        inner_keys.sort()
        inner_keys_list.append(inner_keys)

    for i in range(1, len(inner_keys_list)):
        # If the number of keys is different.
        if len(inner_keys_list[0]) != len(inner_keys_list[i]):
            return False
        # If the keys don't match.
        for j in range(len(inner_keys_list[0])):
            if inner_keys_list[0][j] != inner_keys_list[i][j]:
                return False
    return True
