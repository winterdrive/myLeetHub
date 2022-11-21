class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachPos = 0
        startPos = 0
        while startPos<=reachPos:
            reachPos = max(reachPos,startPos+nums[startPos])
            if reachPos>=len(nums)-1:
                return True
            startPos+=1
        return False