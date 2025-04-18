# To find element which appears more than N/2 times

arr = list(map(int,input("Enter the elements\n").split()))
count = 0



for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] == arr[i]:
            count+=1
if count>(len(arr)//2):
    print(arr[i])
else:
    print("No element is > than N/2 times")