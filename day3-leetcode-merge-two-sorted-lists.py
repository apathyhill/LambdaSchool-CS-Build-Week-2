# Problem:
# Merge Two Sorted Lists

# URL: 
# https://leetcode.com/problems/merge-two-sorted-lists/

# Solution:
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_list = []
        
        while l1:
            node_list.append(l1)
            l1 = l1.next
        while l2:
            node_list.append(l2)
            l2 = l2.next
        node_list = sorted(node_list, key=lambda x: x.val)
        
        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]
                
        if len(node_list) > 0:
            return node_list[0]
        else:
            return None