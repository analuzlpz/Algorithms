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

    def inorder_transversal(self):
        if self.left is None and self.right is None:
            return str(self.data)
        else:
            order_left = ""
            order_right = ""
            if self.left is not None:
                order_left = self.left.inorder_transversal()
            if self.right is not None:
                order_right = self.right.inorder_transversal()
            order = order_left + " " + str(self.data) + " " + order_right
            return order

    def postorder_transversal(self):
        if self.left is None and self.right is None:
            return str(self.data)
        else:
            order_left = ""
            order_right = ""
            if self.left is not None:
                order_left = self.left.postorder_transversal()
            if self.right is not None:
                order_right = self.right.postorder_transversal()
            order = order_left + " " + order_right + " " + str(self.data)
            return order

    def preorder_transversal(self):
        if self.left is None and self.right is None:
            return str(self.data)
        else:
            order_left = ""
            order_right = ""
            if self.left is not None:
                order_left = self.left.preorder_transversal()
            if self.right is not None:
                order_right = self.right.preorder_transversal()
            order = str(self.data) + " " + order_left + " " + order_right
            return order



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

root.print_tree()

print("Inorder",root.inorder_transversal())
print("Postorder",root.postorder_transversal())
print("Preorder",root.preorder_transversal())