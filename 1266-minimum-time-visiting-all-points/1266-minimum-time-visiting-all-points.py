class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # result=0
        # current=points[0]
        # for i in range(1,len(points)):
        #     while True:
        #         if points[i][0]>current[0] and points[i][1]>current[1]:#右上
        #             current=[current[0]+1,current[1]+1]
        #             result+=1
        #         elif points[i][0]<current[0] and points[i][1]<current[1]:#左下
        #             current=[current[0]-1,current[1]-1]
        #             result+=1
        #         elif points[i][0]>current[0] and points[i][1]<current[1]:#右下
        #             current=[current[0]+1,current[1]-1]
        #             result+=1
        #         elif points[i][0]<current[0] and points[i][1]>current[1]:#左上
        #             current=[current[0]-1,current[1]+1]
        #             result+=1
        #         elif points[i][0]>current[0] and points[i][1]==current[1]:#右
        #             current=[current[0]+1,current[1]]
        #             result+=1
        #         elif points[i][0]<current[0] and points[i][1]==current[1]:#左
        #             current=[current[0]-1,current[1]]
        #             result+=1
        #         elif points[i][0]==current[0] and points[i][1]>current[1]:#上
        #             current=[current[0],current[1]+1]
        #             result+=1
        #         elif points[i][0]==current[0] and points[i][1]<current[1]:#下
        #             current=[current[0],current[1]-1]
        #             result+=1
        #         elif points[i][0]==current[0] and points[i][1]==current[1]:
        #             break
        # return result
        
        result=0
        current=points[0]
        for i in range(1,len(points)):
            result+=max(abs(points[i][0]-current[0]),abs(abs(points[i][1]-current[1])))
            current=points[i]
        return result
        