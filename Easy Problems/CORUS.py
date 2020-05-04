"""
The first thing that came to my mind after looking at this problem is dictionary

for each query
pending_queue = sum( for each key(value- query(isolation_centers) if   dictionary[key] > query) )
"""

testcase = int(input())
for z in range(testcase):
    dictionary = {}
    N,C = [int(d) for d in input().split()]
    S = input()
    for i in S:
        if i not in dictionary:
            dictionary[i] = 0
        dictionary[i] = dictionary[i] + 1

    for i in range(C):
        num_isolation_centers = int(input())
        print(sum([dictionary[key] - num_isolation_centers  for key in dictionary if dictionary[key]>num_isolation_centers]))
