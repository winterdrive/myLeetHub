class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result=list()
        for i in queries:
            count=0
            for j in points:
                if((j[0]-i[0])*(j[0]-i[0])+(j[1]-i[1])*(j[1]-i[1])<=(i[2])*(i[2])):
                    count+=1
            result.append(count)
        return result
            