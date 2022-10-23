class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result=0
        myLen=len(pref)
        for i in words:
            if len(i)>=myLen and i[0:myLen]==pref:
                result+=1
        return result