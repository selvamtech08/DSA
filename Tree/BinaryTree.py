class Node:
    """Node class for creating new node objects"""
    def __init__(self, value: int) -> None:
        self.data = value
        self.right = None
        self.left = None

class BSTree:
    """Class for creating binary serach tree objects"""    
    def __init__(self) -> None:
        self.root = None
        self.__totalnodes = 0
            
    @property
    def totalnodes(self) -> int:
        return self.__totalnodes
    
    def insert(self, value: int) -> None:
        self.__totalnodes += 1
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while current:
            if current.data > value:
                if current.left is None:
                    current.left = Node(value)
                else:
                    current = current.left
            elif current.data < value:
                if current.right is None:
                    current.right = Node(value)
                else:
                    current = current.right
            else:
                return    

    def minInorder(self, root: Node) -> int:
        current = root
        while current.left:            
            current = current.left
        return current.data
            
    def __deleteNode(self, root: Node, value: int) -> Node:
        if root is None:
            return root
        if value < root.data:
            root.left = self.__deleteNode(root.left, value)
        elif value > root.data:
            root.right = self.__deleteNode(root.right, value)
        else:
            if root.right is None:     
                self.__totalnodes -= 1                                           
                return root.left
            elif root.left is None:
                self.__totalnodes -= 1                                
                return root.right
            else:
                root.data = self.minInorder(root.right)
                root.right = self.__deleteNode(root.right, root.data)
        return root    

    def remove(self, value: int) -> None:
        """Remove the node from tree"""
        if self.root is None:
            raise ValueError("Empty tree found!")
        self.root = self.__deleteNode(self.root, value)                

    def __preorder(self, root: Node) -> None:
        if root is None:
            return
        print(root.data, end=" -> ")
        self.__preorder(root.left)
        self.__preorder(root.right)

    def preorder(self) -> None:
        print("Preorder:\t", end="")
        self.__preorder(self.root)
        print("")

    def __inorder(self, root: Node) -> None:
        if root is None:
            return
        self.__inorder(root.left)
        print(root.data, end=" -> ")
        self.__inorder(root.right)
    
    def inorder(self) -> None:
        print("Inorder:\t", end="")
        self.__inorder(self.root)
        print("")

    def __postorder(self, root: Node) -> None:
        if root is None:
            return
        self.__postorder(root.left)
        self.__postorder(root.right)
        print(root.data, end=" -> ")

    def postorder(self) -> None:
        print("Postorder:\t", end="")
        self.__postorder(self.root)
        print("")

    def search(self, value: int) -> bool:
        """return true if given value found in the tree, or return false"""
        current = self.root
        while current:
            if value < current.data:
                current = current.left
            elif value > current.data:
                current = current.right
            else:
                return True        
        return False

if __name__ == "__main__":
    bst_1 = BSTree()
    bst_1.insert(15)
    bst_1.insert(7)
    bst_1.insert(21)
    bst_1.insert(12)
    bst_1.insert(3)
    bst_1.insert(9)
    bst_1.insert(13)
    bst_1.preorder()
    bst_1.inorder()
    bst_1.postorder()
    print("Remove node")
    bst_1.remove(21)
    bst_1.preorder()
    bst_1.remove(7)
    bst_1.remove(15)
    bst_1.remove(12)
    bst_1.remove(13)
    bst_1.preorder()
    print(bst_1.search(7))
    print(bst_1.search(15))
    print(bst_1.search(9))

