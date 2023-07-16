from node import Node

class LinkedList:
    length = 0
    def __init__(self):
        self.head = None



    def add_first_by_value(self,value):
        self.length += 1
        node = Node(value)
        node.next = self.head
        self.head = node

    def append_recursive(self, value):
        pass


    def append_simple(self, value):
        self.length += 1
        current_node = self.head
        if not current_node:
            self.head = Node(value)
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(value)
        return self

    def append_sorted(self, value):
        self.length += 1
        if not self.head:
            self.head = Node(value)
        else:
            current_node = self.head
            if current_node.value > value:
                self.head = Node(value)
                self.head.next = current_node
            else:
                while current_node.next and current_node.next.value < value:
                    current_node = current_node.next
                new_node = Node(value)
                new_node.next = current_node.next
                current_node.next = new_node

    def remove_first(self):
        self.length -= 1
        if self.head:
            self.head = self.head.next

    def remove_last(self):
        self.length -= 1
        if self.head:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None

    def remove_by_value(self, value):
        self.length -= 1
        if self.head:
            current_node = self.head
            if current_node.value == value:
                self.head = current_node.next
            else:
                while current_node.next and current_node.next.value != value:
                    current_node = current_node.next
                if current_node.next:
                    current_node.next = current_node.next.next

    def clear(self):
        self.length = 0
        while self.head:
            self.head = self.head.next
        del self.head

    def is_exist(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def print_linked_list(self):
        iter_node = self.head
        while iter_node:
            print(f'the value is: {iter_node.value}')
            iter_node = iter_node.next
    @property
    def __len__(self):
        return self.length




if __name__ == '__main__':
    linked_list_1 = LinkedList()
    # linked_list_1.add_first_by_value(2)
    linked_list_1.append_simple(3)
    linked_list_1.append_simple(5)
    linked_list_1.append_simple(7)
    linked_list_1.append_simple(9)
    linked_list_1.append_simple(11)
    linked_list_1.append_simple(13)
    linked_list_1.append_sorted(8)
    linked_list_1.append_sorted(4)
    print(linked_list_1.__len__)
    linked_list_1.print_linked_list()
