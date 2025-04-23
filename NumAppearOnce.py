# here we need to print the number that appears only once in the list

arr = list(map(int,input("Enter the elements\n").split()))

for i in range(len(arr)):
    count = 0
    num = arr[i]  # selecting one number
    for j in range(len(arr)):
        if arr[j] == num:
            count+=1

    if count == 1:
        print("The number which is alone in list is:", num)
    