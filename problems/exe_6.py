#
# This problem was asked by Google.
#
# An XOR linked list is a more memory efficient doubly linked list. Instead of each
# node holding next and prev fields, it holds a field named both, which is a XOR of
# the next node and the previous node. Implement a XOR linked list; it has an
# add(element) which adds the element to the end, and a get(index) which returns
# the node at index.
#
# If using a language that has no pointers (such as Python), you can assume you
# have access to 'get_pointer' and 'dereference_pointer' functions that converts
# between nodes and memory addresses.


class Node:

    def __init__(self, data):
        self.data = data
        self.both = id(data)


    def __repr__(self):
        return str(self.data)

class LinkedList:

    def __init__(self, node):
        self.head = node
        self.tail = node
        self.head.both = 0
        self.tail.both = 0

    def add(self, element):
        self.tail.both ^= id(element.data)
        element.both = id(self.tail.data)
        self.tail = element

    def get(self, index):
        prev_node_address = 0
        result_node = self.head
        for i in range(index):
            next_node_address = prev_node_address ^ result_node.both
            prev_node_address = id(result_node.data)
            result_node = id_map[next_node_address]
        return result_node.data


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    # id_map simulates object pointer values
    id_map = dict()
    id_map[id("a")] = a
    id_map[id("b")] = b
    id_map[id("c")] = c
    id_map[id("d")] = d
    id_map[id("e")] = e

    llist = LinkedList(c)
    llist.add(d)
    llist.add(e)
    llist.add(a)
    print('llist.get(0) = ', llist.get(0))
