class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        new = Node(new_val)
        if (self.root == None):
            self.root = new
        else:
            curr = self.root
            pare = self.root
            while (curr != None):
                pare = curr
                if (new_val < curr.value):
                    curr = curr.left

                else:
                    curr = curr.right
            if (new_val < pare.value):
                pare.left = new
            else:
                pare.right = new

    def printSelf(self):
        # Your code goes here
        print(self.root)
        
    def search(self, find_val):
        # Your code goes here
        while self.root != None:
            if self.root.value == find_val:
                return True
            if self.root.value < find_val:
                self.root = self.root.right
            else:
                self.root = self.root.left
        return False


