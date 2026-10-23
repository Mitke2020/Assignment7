class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def _find(self, node, name):
        """Recursively search for the node with the given name."""
        if node is None:
            return None
        if node.name == name:
            return node
        found = self._find(node.left, name)
        if found:
            return found
        return self._find(node.right, name)

    def insert(self, parent_name, employee_name, side):
        if side not in ("left", "right"):
            print(f"Invalid side '{side}'. Use 'left' or 'right'.")
            return False

        parent = self._find(self.root, parent_name)
        if parent is None:
            print(f"Parent '{parent_name}' not found in the tree.")
            return False

        if side == "left":
            if parent.left is not None:
                print(f"{parent_name} already has a left report ({parent.left.name}).")
                return False
            parent.left = DoctorNode(employee_name)
        else:
            if parent.right is not None:
                print(f"{parent_name} already has a right report ({parent.right.name}).")
                return False
            parent.right = DoctorNode(employee_name)
        return True

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder: ", tree.preorder(tree.root))
    print("Inorder:  ", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

    print("\n--- Edge cases ---")
    tree.insert("Dr. Nobody", "Dr. Lee", "left")    # parent doesn't exist
    tree.insert("Dr. Croft", "Dr. Lee", "middle")   # invalid side
    tree.insert("Dr. Croft", "Dr. Lee", "left")     # spot already taken

    empty = DoctorTree()
    print("Empty tree preorder:", empty.preorder(empty.root))
    empty.insert("Dr. Croft", "Dr. Lee", "left")    # insert into empty tree