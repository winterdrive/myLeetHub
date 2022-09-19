class Solution:
    def reverseWords(self, s: str) -> str:
        # result=""
        # temp=""
        # for i in range(0,len(s)):
        #     if s[i]!=' ' and i!=len(s)-1:
        #         temp+=s[i]
        #     elif i==len(s)-1:
        #         temp+=s[i]
        #         result=result+temp[::-1]
        #     else:
        #         result=result+temp[::-1]+" "
        #         temp=""
        # return result
        
        result=""
        myLsit=s.split(" ")
        for i in myLsit:
            result+=i[::-1]+" "
        return result[:-1]