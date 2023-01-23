# Dylan D'Eloia / intermediate_python_exercises / itsc3155 / 1 - 22 - 2023

def count_letters(string):
    letter_count = {}
    for letter in string.lower():
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

string = input("Enter a string: ")
print(count_letters(string))