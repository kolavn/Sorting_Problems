# Best time to buy and sell stocks
#Maximize the profit
# given prices in the array for day1, day 2......
# for any given ith day, we compare min cost day which is less than ith day

arr = list(map(int,input("Enter the elements\n").split()))

mini = arr[0] #take as minimum element
profit = 0 # no profit no gain

for i in range(1, len(arr)):
    cost = arr[i] - mini
    profit = max(profit, cost)
    mini = min(mini, arr[i])

print(profit)







