# Write a Python program to reverse a string.

# Sample String : "1234abcd"
# Expected Output : "dcba4321"

sample_string = "1234abcd"

def reverse_string():
    temp = ""
    for i in sample_string:
        temp = i + temp
    print("Expected Output :",temp)

reverse_string()
