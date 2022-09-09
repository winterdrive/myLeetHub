class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resultList=list()
        for i in range(1,n+1):
            if i%15==0:
                resultList.append("FizzBuzz")
            elif i%5==0:
                resultList.append("Buzz")
            elif i%3==0:
                resultList.append("Fizz")
            else:
                resultList.append(str(i))
        return resultList