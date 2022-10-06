class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in range(0,len(image)):
            result.append(image[i][::-1])
        # print(result)
        for i in range(0,len(result)):
            for j in range(0,len(result[i])):
                if result[i][j]==0:
                    result[i][j]=1
                else:
                    result[i][j]=0
        # print(result)
        return result