class Solution:
    def firstUniqChar(self, s: str) -> int:
        i=0
        firstTimeList=list()
        multiTimeList=list()
        while(True):
            if i>=len(s):
                break
            if s[i] not in firstTimeList:
                firstTimeList.append(s[i])
                i+=1
            elif s[i] not in multiTimeList:
                multiTimeList.append(s[i])
                i+=1
            else:
                i+=1
        for i in multiTimeList:
            firstTimeList.remove(i)
        if len(firstTimeList)>0:
            return s.find(firstTimeList[0])
        else:
            return -1