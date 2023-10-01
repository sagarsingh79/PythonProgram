class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def find_max_min(self):
        if not self.head:
            return None, None

        max_val = float('-inf')
        min_val = float('inf')
        current = self.head

        while current:
            if current.data > max_val:
                max_val = current.data
            if current.data < min_val:
                min_val = current.data
            current = current.next

        return max_val, min_val


# Example usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(5)
dll.append(20)
dll.append(8)

max_val, min_val = dll.find_max_min()
print("Maximum value:", max_val)
print("Minimum value:", min_val)
