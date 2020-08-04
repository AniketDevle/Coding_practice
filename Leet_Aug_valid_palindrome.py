import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_char = string.ascii_letters + string.digits
        letters = [ch for ch in s if ch in valid_char]
        str = ""
        for i in letters:
            str = str + i
        str = str.lower()
        l = len(str)
        for i in range(int(l/2)):
            if (str[i]!=str[l-1-i]):
                return False
        
        return True
