print('Hello world')

# If statement and If-else
num = 5
if num > 0:
    print("Positive")
else:
    print("Negative")

# For loop
def print_numbers(numbers: list):
    for n in numbers:
        print(n, end=" ")

numbers = [1, 2, 3, 4, 5]
print_numbers(numbers)

# While loop
def countdown(x: int):
    while x > 0:
        print(x, end=" ")
        x -= 1

countdown(3)

# List - Built-in, Mixed data type, Dynamic resizing, as items can be added or removed
my_list = [1, "apple", 3.14, [2, 3, 4]]

# Array
# Not built-in; require importing the array module or using an external library like NumPy
# Can only store items of the same data type, specified at the time of creation
# Dynamic resizing is possible, but not as straightforward as lists
import array
my_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' represents the data type (signed integer)



# List comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)