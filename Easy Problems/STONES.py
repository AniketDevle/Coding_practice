"""
Put all the characters of jewel in set
check if char of string is in set 
"""

testcase = int(input())
for _ in range(testcase):

    J = [i for i in input()]
    jewels = {";"}
    for i in J:
        jewels.add(i)

    S = [i for i in input()]
    count = 0
    for i in S:
        if i in jewels:
            count = count + 1

    print(count)
            
            
