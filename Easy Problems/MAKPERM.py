"""
The problem aske us to change the given sequence in one of the permutaions
of 1 through N.

Using Sets for this will be a very good option over here cause even if the same
value is repeated multiple times it will only be present in set once

For each testcase:
if the arr[i] is less than or equal to N then add it to the set
print(N-len(set))

"""

testcase = int(input())

for z in range(testcase):
    num = int(input())
    arr = [int(a) for a in input().split()]
    s = {0}                            ## if you dont add some value in curly braces python will interpret it as a dictionary and will give a runtime error
    for i in arr:
        if i<=num:
            s.add(i)
    set_length = len(s) - 1
    print(num-set_length)
    
    
