# Leaders means right to the leader element, every one are small

# arr = list(map(int,input("Enter the elements\n").split()))
# new = [] * len(arr)

# for i in range(len(arr)):
#     # leader = True
#     for j in range(i+1, len(arr)):
#         if arr[j] > arr[i]:
#             # leader = False
#             break
#     else:
#         new.append(arr[i])
# print(new)


arr = list(map(int,input("Enter the elements\n").split()))

new = []
maxi = float('-inf')

for i in range(len(arr)-1, 0, -1):
    if arr[i] > maxi:
        maxi = arr[i]
        new.append(maxi)
print(new)