# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    #def isPalindrome(self, head: Optional[ListNode]) -> bool:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]

