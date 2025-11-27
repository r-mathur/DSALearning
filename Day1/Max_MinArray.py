arr = [1,2,8,4,9,6,3,10]

minm = arr[0]
maxm = arr[0]
print(minm)

for i in range(len(arr)):
    if i == 0:
        continue
    if minm > arr[i]:
        print("yes")
        minm = arr[i]

    if maxm < arr[i]:
        maxm = arr[i]

print("Min : ",minm)
print("Max : ",maxm)