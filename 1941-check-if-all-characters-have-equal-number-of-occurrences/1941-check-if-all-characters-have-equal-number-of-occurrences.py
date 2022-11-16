class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        myDict=dict(Counter(s))
        # myDict=dict(sorted(Counter(s).items(), key=lambda item: item[0]))
        repeatNum=0
        for i in myDict.values():
            if repeatNum==0:
                repeatNum=i
            else:
                if repeatNum!=i:
                    return False
        return True