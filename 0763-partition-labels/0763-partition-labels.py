class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        myDict=dict()
        for i in range(len(s)):
            myDict[s[i]]=i
            
        result=list()
        mySize=0
        myEnd=0
        
        for index,value in enumerate(s):
            mySize+=1
            myEnd=max(myEnd,myDict[value])
            
            if myEnd==index:
                result.append(mySize)
                mySize=0
                
        return result
            