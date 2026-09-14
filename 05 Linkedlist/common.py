class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def linked_input_Optimized():
    value = int(input("Enter the value: "))

    head = None
    tail = None

    while value != -1:
        newnode = Node(value)

        if head is None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = newnode

        value = int(input("Enter the value: "))

    return head


def print_LL(head):
    temp = head

    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next

    print("None")
