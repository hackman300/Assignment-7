class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        if self.root is None or side not in ["left", "right"]:
            return
        parent_node = self.find_node(self.root, parent_name)
        if parent_node is None:
            return
        new_node = DoctorNode(child_name)
        if side == "left":
            parent_node.left = new_node
        else:
            parent_node.right = new_node

    def find_node(self, current, name):
        if current is None:
            return None
        if current.name == name:
            return current
        left_result = self.find_node(current.left, name)
        if left_result is not None:
            return left_result
        return self.find_node(current.right, name)

    def preorder(self, node):
        if node is None:
            return []
        result = [node.name]
        result.extend(self.preorder(node.left))
        result.extend(self.preorder(node.right))
        return result

    def inorder(self, node):
        if node is None:
            return []
        result = self.inorder(node.left)
        result.append(node.name)
        result.extend(self.inorder(node.right))
        return result

    def postorder(self, node):
        if node is None:
            return []
        result = self.postorder(node.left)
        result.extend(self.postorder(node.right))
        result.append(node.name)
        return result

if __name__ == "__main__":
    print("***Tree Creation and Traversal***")
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Jack")

    tree.insert("Dr. Jack", "Dr. Mark", "right")
    tree.insert("Dr. Jack", "Dr. Klay", "left")

    tree.insert("Dr. Klay", "Dr. Phil", "left")

    tree.insert("Dr. Phil", "Dr. Carson", "right")
    tree.insert("Dr. Phil", "Dr. Morgan", "left")

    print("Preorder traversal:")
    print(tree.preorder(tree.root))

    print("\nInorder traversal:")
    print(tree.inorder(tree.root))

    print("\nPostorder traversal:")
    print(tree.postorder(tree.root))
