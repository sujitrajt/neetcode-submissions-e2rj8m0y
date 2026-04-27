# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalf = slow.next
        prevNode = None
        slow.next = None

        while secondHalf:
            tempNode = secondHalf.next
            secondHalf.next = prevNode
            prevNode = secondHalf
            secondHalf = tempNode

        first, secondHalf = head, prevNode
        while secondHalf:
            temp1, temp2 = first.next, secondHalf.next
            first.next = secondHalf
            secondHalf.next = temp1
            first, secondHalf = temp1, temp2