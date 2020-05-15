"""
iterate over string:
    add char in dictionary 
    if (occurance[char] > X) :
        then check if K greater than 0:
            if yes -->> remove the added value of char in occurance
            if no->remome added char and break(cause this wont be appropriate sequence)

print(sum of all values in dictionary)
"""

testcase = int(input())
for _ in range(testcase):
    s = input()
    K , X = [int(d) for d in input().split()]
    occur = {}
    for i in s:

        ##adding the char in dictionary occurance
        if i not in occur:
            occur[i] = 0
        occur[i] = occur[i]+1

        ##check if char is valid:
        if(occur[i] > X):
            if(K>0):                    ##act as if the char never came in and reduce number of deletion allowed
                occur[i] = occur[i] - 1
                K = K - 1
            else:
                occur[i] = occur[i] - 1
                break

    ##after this the occur dictionary will only have good prefixes
    print(sum(occur.values()))
            
