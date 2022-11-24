class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # result=0
        # for i in range(len(target)):
        #     for ele in triplets:
        #         if ele[i]==target[i]:
        #             result+=1
        #             break
        # if result==3:
        #     return True
        # else:
        #     return False
        resultSet= set()
        for ele in triplets:
            if ele[0]>target[0] or ele[1]>target[1] or ele[2]>target[2]:
                continue
            else:
                for i in range(len(ele)):
                    if ele[i]==target[i]:
                        resultSet.add(i)
        return len(resultSet)==3
                