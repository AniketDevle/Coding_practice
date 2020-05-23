"""
This a gcd problem

say the input is 1 4 2

then if we start at (0,0)-> (0,2)->(0 , 0) -> (0 , 2) this loop will continue
and you would never go on the odd positions

where as if the input was

1 , 4 , 3  => start at(0,0)->(0,3)->(0,(3 + 3)% 4)=(0 , 2) ->(0 ,(2+3)%4) = (0,1)
and hence we complete the full cycle in 4 moves

the GCD is 1 => we can get a move that will move up one cell in a direction

"""

import math

testcase = int(input())

for _ in range(testcase):

    N , M , K = [int(s) for s in input().split()]

    if((N % K == 0 or M % K == 0) and K != 1):
        print(-1)
        
    else:
        if (math.gcd(N , K ) == 1 and math.gcd(M , K ) == 1):
            print(N * M)
        else:
            print(-1)
