class Solution:
    def grayCode(self, n: int) -> list[int]:
        myList=list()
        myList.append('0')
        myList.append('1') #初始list建立
        for i in range(2,n+1):
            reverseMyLsit=myList[::-1] #建立鏡像list
            for j in range(0,len(myList)):    
                myList[j]='0'+myList[j] #原本的list加上'0'
                reverseMyLsit[j]='1'+reverseMyLsit[j] #鏡像的list加上'1'
            myList=myList+reverseMyLsit #鏡像跟原本的加起來，進入下一個迴圈
        for k in range(0, len(myList)):
            myList[k]=(int(myList[k],2))
        return myList