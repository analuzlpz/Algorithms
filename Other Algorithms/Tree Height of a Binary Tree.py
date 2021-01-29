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

    def depth_tree(self):
        if self.left is None and self.right is None:
            return 0
        else:
            depth_left = 0
            depth_right = 0
            if self.left is not None:
                depth_left = self.left.depth_tree() + 1
            if self.right is not None:
                depth_right = self.right.depth_tree() + 1
            if depth_left > depth_right:
                return depth_left
            else:
                return depth_right


root = Node(3)
root.left = Node(2)
root.left.left = Node(1)
root.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(6)
root.right.right.right = Node(7)
root.print_tree()
print("Depth", root.depth_tree())
