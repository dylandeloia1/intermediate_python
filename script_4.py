# Dylan D'Eloia / intermediate_python_exercises / itsc3155 / 1 - 22 - 2023

def int_input(prompt):
    # this is an infinite loop that runs until an int value is returned to the function
    # the prompt is the parameter for the function
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an int.")

sum = 0
for i in range(5):
    sum += int_input(f"Enter an integer {i+1}: ")

print("The sum is:", sum)