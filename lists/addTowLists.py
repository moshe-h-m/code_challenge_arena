from typing import Optional

from code_challenge_arena.lists.linkedList import LinkedList
from listnode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i = 1
        l1_counter = l1.val
        l1 = ListNode(l1.next.val, l1.next)

        l2_counter = l2.val
        l2 = l2.next

        while l1.next or l2.next:
            multiple = i * 10
            if l1.next:
                l1_counter += l1.val * multiple
                l1 = l1.next
            if l2.next:
                l2_counter += l2.val * multiple
                l2 = l2.next
            i += 1

        final_counter = l2_counter + l1_counter

        new_list = ListNode(final_counter % 10)
        head = new_list

        final_counter = final_counter / 10

        while final_counter:
            new_list_itr = ListNode(final_counter % 10)
            new_list.next = new_list_itr
            new_list = new_list.next
            final_counter = final_counter / 10

        return head









if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    lin_list = LinkedList(s.addTwoNumbers(l1, l2))
    lin_list.print_linked_list()

    print('------------------')

    l1 = ListNode(0)
    l2 = ListNode(0)
    linked_list = LinkedList(s.addTwoNumbers(l1, l2))
    linked_list.print_linked_list()

    print('------------------')

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    linked_list_2 = LinkedList(s.addTwoNumbers(l1, l2))
    linked_list_2.print_linked_list()

    print('------------------')

    l1 = ListNode(5)
    l2 = ListNode(5)
    linked_list_3 = LinkedList(s.addTwoNumbers(l1, l2))
    linked_list_3.print_linked_list()

