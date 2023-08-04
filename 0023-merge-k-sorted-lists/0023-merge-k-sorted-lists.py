# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Wrapper():
            def __init__(self,node):
                self.node = node
            def __lt__(self,other):
                return self.node.val<other.node.val
        head = point = ListNode(0)
        q=[]
        for l in lists:
            if l:
                heapq.heappush(q,Wrapper(l))
        while q:
            node = heapq.heappop(q)
            point.next = node.node
            point = point.next
            node = node.node.next
            if node:
                heapq.heappush(q,Wrapper(node))
        return head.next