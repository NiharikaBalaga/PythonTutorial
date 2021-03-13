myDict = {
    "1": "Fan",
    "2": "Box",
    "3": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the number\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))