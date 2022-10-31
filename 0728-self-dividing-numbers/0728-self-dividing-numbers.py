def selfDivide(num):
    result=True
    for i in str(num):
        if int(i)==0 or num%int(i)!=0:
            result=False
    return result

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        myList=list()
        for i in range(left,right+1):
            if selfDivide(i):
                myList.append(i)
        print(myList)
        return myList