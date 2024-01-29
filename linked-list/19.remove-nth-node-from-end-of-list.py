# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # time: O(N)
        # space: O(1)
        dummy = ListNode(0, head)
        itr, end = dummy, dummy

        while n > 0:
            end = end.next
            n -= 1

        while end.next:
            end = end.next
            itr = itr.next

        if itr:
            itr.next = itr.next.next
        
        return dummy.next