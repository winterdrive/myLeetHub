class Solution:
    def countAsterisks(self, s: str) -> int:
        result=0
        myList=s.split("|")
        for i in range(0,len(myList),2):
            for j in myList[i]:
                if j=="*":
                    result+=1
        return result