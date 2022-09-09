class Solution:
    def minimumSum(self, num: int) -> int:
        myString=sorted(list(str(num)))
        return int(myString[0]+myString[2])+int(myString[1]+myString[3])

            