class Solution:
    def grayCode(self, n: int) -> List[int]:
        myList=list()
        myList.append('0')
        myList.append('1')
        currentLength=len(myList)
        for i in range(2,n+1):
            reverseMyLsit=myList[::-1]
            for j in range(0,len(myList)):    
                myList[j]='0'+myList[j]
                reverseMyLsit[j]='1'+reverseMyLsit[j]
            myList=myList+reverseMyLsit
        result=list()
        for k in range(0, len(myList)):
            result.append(int(myList[k],2))
        return result