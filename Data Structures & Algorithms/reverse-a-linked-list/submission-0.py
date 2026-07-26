# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next  # (2,3,4,null) (3,4, null) (4, null)
            curr.next = prev # (null) (1, null) ()
            prev = curr      # (1, null) (2, 3, 4, null)
            curr = nxt       # (2,3,4, null) (3,4, null)    
        
        return prev
