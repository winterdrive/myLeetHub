class Solution:
    def removePalindromeSub(self, s: str) -> int:
        frontIndex=0
        endIndex=-1
        for i in range(len(s)):
            if s[frontIndex+i]==s[endIndex-i]:
                continue
            else:
                return 2
        return 1
        