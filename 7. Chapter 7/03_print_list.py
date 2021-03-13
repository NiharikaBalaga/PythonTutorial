# fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i = i+1

# bike = ['KTM','RE','FZ','Hero','Bajaj']

# i=0
# while i<len(bike):
#     print(bike[i])
#     i=i+1
num = 16

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    while(num > 0):
            sum += num
            num -= 1
    print("The sum is", sum)
