# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
# Each employee information consists of Name, DOB, Height, City, State. 
# Write a python program that reads this information from the JSON file and 
# saves the information into a list of objects of Employee class. 
# Finally print the list of the Employee objects.


import json

employee = {'employee_1':{"name": "Hrith Biswas","dob": "1996-02-02","height": 169,"city": "Patna","state": "Bihar"},
             'employee_2':{"name": "Smriti Patel","dob": "1965-06-15","height": 152,"city": "Mumbai","state": "Maharashtra"},
             'employee_3':{"name": "Harsh Gupta","dob": "1999-09-08","height": 167,"city": "New Delhi","state": "Delhi"},
             'employee_4':{"name": "Vedant Patil","dob": "1997-07-03","height": 160,"city": "Lucknow","state": "U.P"},
             'employee_5':{"name": "Ankit Pal","dob": "1983-04-04","height": 172,"city": "Ujjain","state": "M.P"}}
print(employee)
with open('employee.json','w') as file:
    json.dump(employee,file,indent = 4)
    print("json completed")


with open("employee.json",'r') as f:
    employees = json.load(f)
for i in employees:
    print(i)

