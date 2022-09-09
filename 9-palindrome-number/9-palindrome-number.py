class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        for i in range(0,len(x)):
            if x[i]==x[-1-i]:
                pass
            else:
                return False
        return True