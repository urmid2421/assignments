# Write a Python function that accepts a string and calculate the number of upper case letters 
# and lower case letters.

# Sample String : 'The quick Brow Fox'

# Expected Output :
#     No. of Upper case characters : 3
#     No. of Lower case Characters : 12

sample_string = 'The quick Brow Fox'

def uppercase_lowercase():
    count_upper = 0
    count_lower = 0 
    for i in sample_string:
        if i.isupper():
            count_upper += 1
        if i.islower():
            count_lower += 1 
    print("No. of upper case characters :",count_upper)
    print("No. of lower case characters : ",count_lower)

uppercase_lowercase()
