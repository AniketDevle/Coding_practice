"""
Find difference and change one digit

add one to the difference

but adding 1 to 9 will change two digits so if (ans % 10 == 9 ) subtract one
from ans 
"""

A , B = [int(d) for d in input().split()]

ans = abs(A-B)

if(ans % 10 == 9):
    ans = ans-1
else:
    ans = ans + 1

print(ans)    
