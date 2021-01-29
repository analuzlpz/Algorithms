import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_tree(self):
        print("node", self.data)
        if self.left is not None:
            print(self.data, "left →")
            self.left.print_tree()
        if self.right is not None:
            print(self.data, "right →")
            self.right.print_tree()

    def level_order(self):
        order = ""

        q = queue.Queue()
        q.put(self)

        while not q.empty():
            element = q.get()
            order = order + " " + str(element.data)
            if element.left is not None:
                q.put(element.left)
            if element.right is not None:
                q.put(element.right)
        return order

root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)

root.print_tree()
print("level order", root.level_order())