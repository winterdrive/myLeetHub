class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict={}
        tSet=set()
        for i in (range(0,len(s))):
            if s[i] not in dict :
                if t[i] not in tSet:
                    dict[s[i]]=t[i]
                    tSet.add(t[i])
                else:
                    return False
                pass 
            if dict[s[i]]!=t[i]:
                return False
        return True