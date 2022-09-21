class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result=0
        myDict=dict()
        myDict['type']=0
        myDict['color']=1
        myDict['name']=2
        for i in items:
            if i[myDict[ruleKey]]==ruleValue:
                result+=1
        return result