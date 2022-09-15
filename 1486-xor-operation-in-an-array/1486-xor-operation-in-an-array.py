class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # 法一        
        # result=0
        # myList=list()
        # for i in range(0,n):
        #     myList.append(start+i*2)
        # result=myList[0]
        # for i in range(1,len(myList)):
        #     result=result^myList[i]
        # return result
        
        # 法二        
        result=start
        for i in range(1,n):
            result=result^(start+i*2)
        return result
        