"""


"""
import string 
class Solution:

    def upper_lower_digit(self ,s):
        """
        this Function return an array which tells us if upper of lower is present or not
        Uppercase is present then first element of return arraywill be 1 else 0
        Lowercase is present then second element of return arraywill be 1 else 0
        Digit is present then Third element of return arraywill be 1 else 0
        """
        lower_char = string.ascii_lowercase
        upper_char = string.ascii_uppercase
        digits = string.digits

        upper_present = 0
        lower_present = 0
        digit_present = 0
        for i in s:
            if i in lower_char:
                lower_present = 1
            elif i in upper_char:
                upper_present = 1
            elif i in digits:
                digit_present = 1
        return [upper_present ,lower_present , digit_present]
        
    def less_than_six(self,s):
        """
        
        length = len(s)
        If length< 2 : we can arrange the characters as we wish and we dont need to make any changes
        If length == 3: say s is "aaa" -> you earlier thought of changing the s[-1] and then adding 3 different required values but this is wrong
        -> Inserting between the second and third character will add element and will make required change as well like insert 1 then s will be "aa1a"

        what if all the character is s are symbols: s = "..."
        -> add 1 in between  => s = "..1."
        -> add lowercase and uppercase => s = "..1.aA"
        
        so if length < 4:
                    return 6-length

        what if the length between (4,5):
        say s = "aaaa" -> check if lowercase or uppercase or digit (ie upper_present + lower_present + digit_present > 1) is present if yes the simply return 2
        but if s = "...." -> no upper or lower or digit so (upper_present + lower_present + digit_present == 0) then you need to add all 3 so return 3

        so return max( length required to reach 6  , absence of upper,lower,digit)
            
        """
        length = len(s)
        if length < 4:
            return 6-length
        else:
            
            return max(6-length , 3- sum(self.upper_lower_digit(s)))        
                
                
    def accurate_length(self, s ,smaller = False):
        """
        Now you need to think about the length at all
        it is assumed that the input of this function will have length between 6 and 20

        Now you need to think about two things
        1 -> all lowercase,uppercase, digit are present
        2 -> No of three similar cases present 

        count will measure the maximum occurance of 'aaa' type elements
        """
        
        password  = s
        count = 0
        index = 2
        arr = []
        while (index < len(s)):
            if password[index] == password[index-1] and password[index-1] == password[index-2]:
                count = count + 1
                arr.append(index)
                index = index + 3
                
            else:
                index = index + 1
        if smaller:
            return max(count ,3- sum(self.upper_lower_digit(s)))
        else:
            return [max(count ,3- sum(self.upper_lower_digit(s))) , arr]
        

    def len_greater(self ,s):
        """
        The length of s is greater than 20 so we need to delete len(s)-20 elements to get a string that has size 20 which is valid
        Then for every valid string of length 20 find a string in which we need to make minimum number of changes
        we call accurate length function over here cause we knew we were only goint to input string that had length less than 20 in it
        """
        mini = 100000000000
        left = -1000000
        right = 1000000
        
        for i in range (len(s)-20+1):
            check = self.accurate_length(s[i:i+20]) 
            if  check[0] < mini:
                left = i
                right = i+20
                mini = check[0]
                brr = check[1]
                for j in range(len(brr)):
                    brr[j] = brr[j] + i

        in_between = 0
        for i in range(len(brr)):
            if brr[i]>= left and brr[i] <=right:
                in_between = in_between+1
        
            
                
        return (len(s) - 20 + mini - in_between)        
             
            
            


        
    def strongPasswordChecker(self, s:str) -> int:
        length = len(s)
        if length< 6:
            return self.less_than_six(s) 
        elif length>5 and length<21:
            return self.accurate_length(s , True)
        else:
            return self.len_greater(s)
        




a = "..A1a"
b = ".................sss"
c = "1010101010aaaB10101010"


K = Solution()
print(K.strongPasswordChecker(c))

