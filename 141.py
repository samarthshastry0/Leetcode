# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        tracker = set()
        tracker.add(head)

        while head != None:
            if head.next in tracker:
                return True
            
            tracker.add(head.next)
            head = head.next
        return False


