"""
Operations available
1. Any pile -> Box
2. Box -> any pile

algo
1.Find the Maximum number of piles with the same number of coins
2.Num of steps required will be total piles - max number with same number 

This problem would have been dificult if we were allowed to change only one tile
at a time

"""

testcase = int(input())
for z in range(testcase):
    num = int(input())
    arr = [int(d) for d in input().split()]
    Dictionary = {}
    for i in arr:
        if i not in Dictionary:
            Dictionary[i] = 0
        Dictionary[i] = Dictionary[i] + 1
    max_with_same = max([Dictionary[key] for key in Dictionary])
    print(num - max_with_same)
