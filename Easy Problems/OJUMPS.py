"""

This looks like an easy problem
The total numbe rof steps that he will take in 3 jumps is 6
so find rem = (a%6)
Then he can move from {0 , 1 , 3} only 

"""

num = int(input())
rem = num % 6

if rem in [0 , 1 , 3]:
    print("yes")
else:
    print("no")
