#reverse a array

arr = [1,2,4,5,6,7]
print("Original Array : ",arr)
res = []
length = len(arr)

for i in range(length):
    index = (length - i)-1
    res.append(arr[index])

print("Reversed Array : ",res)
