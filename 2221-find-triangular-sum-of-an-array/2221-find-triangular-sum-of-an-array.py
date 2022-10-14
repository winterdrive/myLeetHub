def addMyList(myList):
        newList=list()
        if(len(myList)==1):
            return myList
        for i in range(len(myList)):
            if(i==len(myList)-1):
                continue
            else:    
                newList.append(myList[i]+myList[i+1])
        if len(newList)>1:
            return addMyList(newList)
        else:
            return newList
class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        result=addMyList(nums)
        print(result[0]%10)
        return result[0]%10