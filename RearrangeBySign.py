#given equal no of +ve and -ve numbers
# rearrange by sign + - + - + -

# arr = list(map(int,input("Enter elements:\n").split()))
# pos = []
# neg = []

# for i in range(len(arr)):
#     if arr[i]>0:
#         pos.append(arr[i])
#     if arr[i] < 0:
#         neg.append(arr[i])

# for i in range(len(arr)//2):
#     arr[2*i] = pos[i]
#     arr[2*i+1] = neg[i]

# print(pos)
# print(neg)
# print(arr)

############## 2nd version Optimal 

arr = list(map(int,input("Enter elements:\n").split()))
new = [0] * len(arr)
posIndex = 0  # since +ve numbers occupy even places 0, 2, 4
negIndex = 1 # since negative numbers occupy odd places 1, 3, 5

for i in range(0, len(arr)):
    if arr[i] > 0:
        new[posIndex] = arr[i]
        posIndex += 2
    else:
        new[negIndex] = arr[i]
        negIndex+=2
print(new)