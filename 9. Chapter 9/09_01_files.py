# # Use open function to read the content of a file!
# f = open('sample.txt', 'w')
# # f = open('sample.txt')  # by default the mode is r
# # data = f.read()
# data = f.read(5)  # reads first 5 characters from the file
# print(data)
# f.close()

f = open("neha.text", "w")
f.write("Hey hello")
f.write("Hey hello")
f.write("Hey hello")
print(f)
f.close()
