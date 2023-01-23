# Dylan D'Eloia / intro_python_exercises / itsc3155 / 1 - 13 - 2023

def unique_list(lst):
    new_list = list(set(lst))
    return new_list

my_list = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8]
print(unique_list(my_list))

