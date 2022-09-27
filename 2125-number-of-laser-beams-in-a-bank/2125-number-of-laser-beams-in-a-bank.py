class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result=0
        newList=[]
        for i in bank:
            if i.count("1")!=0:
                newList.append(i.count("1")) 
        for i in range(0,len(newList)):
            if (i+1)==len(newList):
                break
            result+=newList[i]*newList[i+1]
        return result