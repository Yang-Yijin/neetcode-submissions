"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        d = {}
        curr = head
        while curr:
            if curr not in d:
                d[curr] = Node(curr.val,None,None)
            if curr.next:
                if curr.next not in d:
                    d[curr.next] = Node(curr.next.val,None,None)
                d[curr].next = d[curr.next]
            if curr.random:
                if curr.random not in d:
                    d[curr.random] = Node(curr.random.val,None,None)
                d[curr].random = d[curr.random]
            curr = curr.next
        return d[head]