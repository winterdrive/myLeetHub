class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        result=""
        myLast=list()
        myList=list()
        for i in paths:
            if i[0] not in myList:
                myList.append(i[0])    
            else:
                myList.remove(i[0])
            if i[1] not in myList:
                myList.append(i[1])
                myLast.append(i[1])   
            else:
                myList.remove(i[1])
        for i in myList:
            if i in myLast:
                result=i
        # print(result)
        return result