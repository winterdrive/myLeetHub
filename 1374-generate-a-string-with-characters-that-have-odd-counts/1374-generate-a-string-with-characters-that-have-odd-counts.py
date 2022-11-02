class Solution:
    def generateTheString(self, n: int) -> str:
        result=""
        if n%2==0:#偶數
            result+="a"*(n-1)
            result+="b"
        else:#奇數
            result+="a"*(n)
        # print(result)
        return result