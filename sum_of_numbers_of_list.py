#  Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# Explanation:
# Summation should like 8+2+3+0+7 = 20

sample_list = (8,2,3,0,7)

count = 0
for i in sample_list:
    count += i
print("Expected ouput :",count)