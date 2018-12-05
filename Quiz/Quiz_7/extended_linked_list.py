# Written by Kun Zhang for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self, step):

        # loop the list
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = self.head

        # get new self head
        node = self.head
        for i in range(step-1):
            node = node.next_node
        self.head = node

        t_node = node
        loop_offset = 0

        while loop_offset != step :
            i = 0
            while i < (step - loop_offset):
                t_node = t_node.next_node
                if i == step - loop_offset - 2:
                    prev_node = t_node
                if t_node == self.head:
                    loop_offset += 1
                    i -= 1
                i += 1

            if node == self.head:
                node = t_node
                second_node = t_node
            else:
                old_node = node
                node.next_node = t_node
                node = node.next_node

            prev_node.next_node = node.next_node

        self.head.next_node = second_node
        old_node.next_node = None


















