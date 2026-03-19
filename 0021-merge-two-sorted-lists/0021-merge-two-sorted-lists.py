# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 方法一
        # 時間複雜度：O((N+M)log(N+M))。
        # 空間複雜度：O(N+M)。
        # list1_list = list()
        # while list1:
        #     list1_list.append(list1.val)
        #     list1 = list1.next
        # list2_list = list()
        # while list2:
        #     list2_list.append(list2.val)
        #     list2 = list2.next
        # list_sum = sorted(list1_list + list2_list)
        # init_node = ListNode(0)
        # ans_list = init_node
        # for idx, ele in enumerate(list_sum):
        #     ans_list.next = ListNode(ele)
        #     ans_list = ans_list.next
        # return init_node.next

        # 方法二
        init_node = ListNode(0)
        curr = init_node

        while list1 and list2:
            if list1.val >= list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            # 「只寫 .next 是看風景，寫了 = .next 才是往前行。」
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return init_node.next
