class Solution:
    def isValid(self, s: str) -> bool:
        Dict = {
                ')' : '(' ,
                '}' : '{' ,
                ']' : '[' 
               }
        arr = []
        b = ['{' , '(' , '[']    
        try:
            for i in range(len(s)):
                if (len(arr) == 0):
                    arr.append(s[i])
            
                else:
                    if s[i] not in b:
                        if arr[-1] == Dict[s[i]] :
                            arr.pop()
                   
                        else:
                         arr.append(s[i])
                    
                    else:
                        arr.append(s[i])
                
            if(len(arr)!=0):
                return (False)
            else:
                return( True)
            
        except:
            return(False)
                
