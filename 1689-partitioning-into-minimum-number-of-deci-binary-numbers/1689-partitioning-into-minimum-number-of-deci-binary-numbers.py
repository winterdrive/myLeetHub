class Solution:
    def minPartitions(self, n: str) -> int:
        # 法一
        # result=0
        # for i in n:
        #     if int(i)>result:
        #         result=int(i)
        # return result
        # 法二
        return sorted(n)[-1]
        # 法三
        # return max(n)