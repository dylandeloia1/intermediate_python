# Dylan D'Eloia / intermediate_python_exercises / itsc3155 / 1 - 22 - 2023

def get_combined_dicts(dict1, dict2):
    combined = {}
    for key in dict1:
        if key in dict2:
            combined[key] = dict1[key] + dict2[key]
    return combined

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dicts(my_dict_1, my_dict_2)
print(combined_dict)