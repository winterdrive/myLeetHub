class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_list = set(nums)
        current_element = None
        for index, element in enumerate(nums):
            if element!=current_element:
                current_element=element
            else:
                nums[index] = 101
        nums = nums.sort()
        
        return len(num_list)
