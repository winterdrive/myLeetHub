class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n==1:
            return 1
        myList=[*range(1,n+1)]
        nowNum=k
        nowIndex=myList.index(nowNum)
        myList.remove(nowNum)
        nowIndex-=1
        while len(myList)!=1:
            if nowIndex+k<len(myList):
                nowIndex+=k
            else:
                nowIndex=(nowIndex+k)%len(myList)
            myList.remove(myList[nowIndex])
            nowIndex-=1
        # print(myList[0])
        return myList[0]