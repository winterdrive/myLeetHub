class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result=0
        for i in words:
            for j in range(0,len(i)):
                if i[j] not in allowed:
                    break
                if j==len(i)-1:
                    result+=1
        return result
                
                