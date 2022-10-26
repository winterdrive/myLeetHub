class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        myLen=len(s)
        for i in range(len(s)):
            current=s[0]
            s.insert(myLen-i,current)
            s.pop(0)