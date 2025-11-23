'''
19. Remove Nth Node From End of List 


Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
'''

#solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         # Create a dummy node to handle edge cases
        res = ListNode(0, head)
        dummy = res

        # Move the head pointer n steps forward
        for _ in range(n):
            head = head.next

        # Move both pointers until head reaches the end
        while head:
            head = head.next
            dummy = dummy.next

        # Remove the nth node from the end
        dummy.next = dummy.next.next

        # Return the updated list
        return res.next

