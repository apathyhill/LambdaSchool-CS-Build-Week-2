# Problem:
# Add Two Numbers

# URL: 
# https://leetcode.com/problems/add-two-numbers/

# Solution:
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_orig = ListNode(0) # Create a start point for our output ListNode
        node = node_orig # Set current node to start
        extra = 0 # Used for carrying to the next place
        while l1 or l2 or extra > 0: # While there are values in the input ListNodes left, or there is a carry amount
            d1 = l1.val if l1 else 0 # Get values if ListNodes are not None else be 0
            d2 = l2.val if l2 else 0
            d3 = d1 + d2 + extra # Add current digit up
            digit = d3 % 10 # Get actual digit (ex: 13 % 10 == 3)
            extra = d3 // 10 # Get carry amount (ex: 13 // 10 == 1)
            node.next = ListNode(digit) # Set next node to digit
            node = node.next # Set current node to next node
            if l1: # Keep iterating through ListNodes until they are None
                l1 = l1.next
            if l2:
                l2 = l2.next
        return node_orig.next # Return output ListNode from starting point's next node