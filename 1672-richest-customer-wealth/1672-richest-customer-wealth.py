class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result=0
        for i in accounts:
            if sum(i)> result:
                result=sum(i)
        return result