# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while not fast == None and not fast.next == None:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        prev = None
        current = second_half
        while not current == None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        first = head
        second = prev

        temp = head
        while temp:
            print(temp.val)
            temp = temp.next

        while not second == None:
            next = first.next
            first.next = second
            next2 = second.next
            second.next = next
            first = next
            second = next2