a = "1"
b = "1111"

lena = len(a)
lenb = len(b)
if lena> lenb:
    zeros = "0"* (lena-lenb)
    b = zeros+b
if lena < lenb:
    zeros = "0"* (lenb-lena)
    a = zeros+a
a = a[::-1]
b = b[::-1]

carry = 0
ans = ""
        
for i in range(len(a)):
    a_val = int(a[i])
    b_val = int(b[i])
            
    if (a_val + b_val + carry == 0):
        ans = ans + "0"
        carry = 0
    elif (a_val + b_val + carry == 1):
        ans = ans + "1"
        carry = 0
    elif (a_val + b_val + carry == 2):
        ans = ans + "0"
        carry = 1
    else :
        ans = ans + "1"
        carry = 1
        
if carry ==1:
    ans = ans + "1"

print(ans[::-1])
