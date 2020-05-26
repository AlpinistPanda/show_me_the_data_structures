class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_list = []
        while cur_head:
            out_list.append(str(cur_head.value))
            cur_head = cur_head.next
        return "->".join(out_list)

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(linklist1, linklist2):
    s_llist = set()
    union_llist = LinkedList()
    node1 = linklist1.head
    while node1:
        s_llist.add(node1.value)
        node1 = node1.next
    node2 = linklist2.head
    while node2:
        s_llist.add(node2.value)
        node2 = node2.next
    for value in s_llist:
        union_llist.append(value)
    return union_llist if union_llist.head is not None else "No union"


def intersection(linklist1, linklist2):
    intersection_llist = LinkedList()
    s_llist1 = set()
    s_llist2 = set()
    node1 = linklist1.head
    while node1:
        s_llist1.add(node1.value)
        node1 = node1.next

    node2 = linklist2.head
    while node2:
        s_llist2.add(node2.value)
        node2 = node2.next
    intersection = s_llist1 & s_llist2
    for value in intersection:
        intersection_llist.append(value)
    return intersection_llist if intersection_llist.head is not None else "No intersection"


print('Case 1')
print('==========================================')

linkedlist1 = LinkedList()
linkedlist2 = LinkedList()

element1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]

for i in element1:
    linkedlist1.append(i)

element2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element2:
    linkedlist2.append(i)

# print union of two linked lists
print(union(linkedlist1, linkedlist2))
# print intersection of two linked lists
print(intersection(linkedlist1, linkedlist2))

print('\n')
print('Case 2')
print('==========================================')

linkedlist3 = LinkedList()
linkedlist4 = LinkedList()

element1 = [9, 15, 5, 23, 8]


for i in element1:
    linkedlist3.append(i)

element2 = [8, 2, 5, 11, 8]

for i in element2:
    linkedlist4.append(i)

# print union of two linked lists
print(union(linkedlist3, linkedlist4))
# print intersection of two linked lists
print(intersection(linkedlist3, linkedlist4))

print('\n')
print('Case 3')
print('==========================================')

linkedlist5 = LinkedList()
linkedlist6 = LinkedList()

element1 = []

for i in element1:
    linkedlist5.append(i)

element2 = [1]
for i in element2:
    linkedlist6.append(i)

# print union of two linked lists
print(union(linkedlist5, linkedlist6))
# print intersection of two linked lists
print(intersection(linkedlist5, linkedlist6))

linkedlist7 = LinkedList()
linkedlist8 = LinkedList()

element1 = []


for i in element1:
    linkedlist7.append(i)

element2 = []

for i in element2:
    linkedlist8.append(i)

# print union of two linked lists
print(union(linkedlist7, linkedlist8))

# print intersection of two linked lists
print(intersection(linkedlist7, linkedlist8))
