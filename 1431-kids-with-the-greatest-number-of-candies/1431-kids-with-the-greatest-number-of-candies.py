class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatestNumber=max(candies)
        result=list()
        for i in candies:
            if i+extraCandies>=greatestNumber:
                result.append(True)
            else:
                result.append(False)
        return result