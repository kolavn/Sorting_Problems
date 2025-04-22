arr = list(map(int,input("Enter elements:\n").split()))
temp = []
for i in range(len(arr)):
    if arr[i]!=0:
        temp.append(arr[i])
for i in range(len(temp)):
    arr[i] = temp[i]
for i in range(len(temp), len(arr)-1, 1):
    arr[i] = 0
print(arr)


