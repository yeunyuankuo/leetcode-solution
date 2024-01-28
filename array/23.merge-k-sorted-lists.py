# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # time: O(NlogK)
        # space: O(K), k is the number of lists to merge
        if not lists or len(lists) == 0:
            return None
        
        heap = []
        for i, l in enumerate(lists):
            if l:
                # we use tuple (l.val, i , l) to store in minheap
                # l.val is the value used as the min heap comparison value
                # i is to distinguish different lists (heapq cannot directly compare ListNode; hence we need this i value)
                # l is the list itself
                heapq.heappush(heap, (l.val, i, l))
        
        dummy = ListNode()
        tail = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next