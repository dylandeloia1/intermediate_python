# Dylan D'Eloia / intermediate_python_exercises / itsc3155 / 1 - 22 - 2023

def get_unique_list(lst):
    new_list = list(set(lst))
    return new_list

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)