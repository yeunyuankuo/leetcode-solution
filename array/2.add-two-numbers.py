# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # time: O(N)
        # space: O(N)
        exceed = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            sum = l1.val + l2.val + exceed
            exceed = 0
            if sum >= 10:
                exceed = 1
            curr.next = ListNode(sum % 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        itr = l1 or l2
        while itr:
            sum = exceed + itr.val
            exceed = 0
            if sum >= 10:
                exceed = 1
            curr.next = ListNode(sum % 10)
            curr = curr.next
            itr = itr.next
        
        if exceed > 0:
            curr.next = ListNode(1)