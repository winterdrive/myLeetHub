# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_list = list()
        while list1:
            list1_list.append(list1.val)
            list1 = list1.next
        list2_list = list()
        while list2:
            list2_list.append(list2.val)
            list2 = list2.next

        list_sum = sorted(list1_list + list2_list)
        init_node = ListNode(0)
        ans_list = init_node
        for idx, ele in enumerate(list_sum):
            ans_list.next = ListNode(ele)
            ans_list = ans_list.next

        return init_node.next