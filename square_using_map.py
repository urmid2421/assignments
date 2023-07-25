# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]
# Square the elements of the list: [16, 25, 4, 81]

def square(num):
    return num**2

sample_list = [4, 5, 2, 9]

result = list(map(square,sample_list))
print("Output = ", result)
