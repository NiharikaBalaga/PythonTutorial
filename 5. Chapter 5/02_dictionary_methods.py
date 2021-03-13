myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'Niha': 'Player'},
    1: 2
}

# Dictionary Methods

# print(myDict)
# print(list(myDict.keys())) # Prints the keys of the dictionary
# print(myDict.values()) # Prints the keys of the dictionary 
# print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
# print(myDict)
# myfriends = {
#     "Lovish": "Friend",
#     "Divya": "Friend",
#     "Shubham": "Friend",
#     "harry": "A Dancer",
#     "fast":"Python"
# }
# myDict.update(myfriends) # Updates the dictionary by adding key-value pairs from updateDict
# print(myDict)

print(myDict.get("dino")) # Prints value associated with key "harry"
# print(myDict["dino"]) # Prints value associated with key "harry"

# # The difference between .get and [] sytax in Dictionaries?
# print(myDict.get("happy2")) # Returns None as harry2 is not present in the dictionary
# print(myDict["happy2"]) # throws an error as harry2 is not present in the dictionary
