from typing import Optional

from code_challenge_arena.lists.linkedList import LinkedList
from node import Node

class Solution:
    def addTwoNumbers(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        array_l1 = []
        array_l2 = []

        if not l1.next or not l2.next and l1.value + l2.value >= 10:
            array_l1.append(l1.value)
            array_l2.append(l2.value)

        while l2.next or l1.next:
            if l1.next:
                array_l1.append(l1.value)
                l1 = l1.next
            if l2.next:
                array_l2.append(l2.value)
                l2 = l2.next

        print(array_l1), print(array_l2)
        array_l1.append(l1.value)
        array_l2.append(l2.value)

        new_linked_list = None
        buffer = 0

        while array_l1 or array_l2:
            if array_l1 and array_l2:
                sum_nums = array_l1.pop() + array_l2.pop()
            elif array_l1:
                sum_nums = array_l1.pop()
            else:
                sum_nums = array_l2.pop()
            new_linked_list = Node(sum_nums % 10 + buffer, new_linked_list)
            buffer = sum_nums // 10


        return new_linked_list





if __name__ == '__main__':
    s = Solution()
    l1 = Node(7, Node(2, Node(4, Node(3))))
    l2 = Node(5, Node(6, Node(4)))
    lin_list = LinkedList(s.addTwoNumbers(l1, l2))
    lin_list.print_linked_list()

    print('------------------')

    l1 = Node(0)
    l2 = Node(0)
    linked_list = LinkedList(s.addTwoNumbers(l1, l2))
    linked_list.print_linked_list()

    print('------------------')

    l1 = Node(9, Node(9, Node(9, Node(9, Node(9, Node(9, Node(9)))))))
    l2 = Node(9, Node(9, Node(9, Node(9))))
    linked_list_2 = LinkedList(s.addTwoNumbers(l1, l2))
    linked_list_2.print_linked_list()

    print('------------------')

    l1 = Node(5)
    l2 = Node(5)
    linked_list_3 = LinkedList(s.addTwoNumbers(l1, l2))
    linked_list_3.print_linked_list()

