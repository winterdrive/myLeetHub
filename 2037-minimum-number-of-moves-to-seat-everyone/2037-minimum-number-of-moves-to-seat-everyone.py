class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result=0
        seats=sorted(seats)
        students=sorted(students)
        for i in range(0,len(seats)):
            result+=abs(seats[i]-students[i])
        # print(result)
        return result