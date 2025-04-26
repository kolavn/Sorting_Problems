#Sort an arry which has only 0,1,2

arr = list(map(int,input("Enter the elements\n").split()))
count0 = 0
count1 = 0
count2 = 0

for i in range(len(arr)):
    if arr[i] == 0:
        count0+=1
    if arr[i] == 1:
        count1+=1
    if arr[i] == 2:
        count2+=1
for i in range(0,count0):
    arr[i] = 0
for i in range(count0+1, count0+count1):
    arr[i] = 1
for i in range(count0+count1+1, len(arr)):
    arr[i] = 2

print(arr)
    