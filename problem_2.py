# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json
states_and_capitals_of_India = {
    "West Bengal": "Kolkata",
    "Himachal Pradesh": "Shimla",
    "Tamil Nadu": "Chennai",
    "Maharashtra": "Mumbai",
    "Rajasthan": "Jaipur",
    "Gujarat": "Gandhinagar",
    "Uttar Pradesh": "Lucknow"
}


with open("states_and_capitals.json", "w") as file:
    json.dump(states_and_capitals_of_India, file, indent=4)

print("Data written to  successfully.")
