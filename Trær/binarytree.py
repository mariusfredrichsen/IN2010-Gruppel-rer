

# en klasse node for å holde på pekere til venstre og høyre og data
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)


# en klasse tree for å holde på nodene
class BinaryTree:
    def __init__(self):
        self.root = None
    
    # metode for å sette inn nye noder
    def insert(self, data, v):
        if v == None:
            v = Node(data)
            if self.root == None:
                self.root = v
        
        elif v.data > data:
            v.left = self.insert(data, v.left)
        
        elif v.data < data:
            v.right = self.insert(data, v.right)
        
        return v

    # metode for å visalisere treet med dybde på hver node
    def print_out(self, v, d = 0):
        if v == None:
            return
        self.print_out(v.left, d+1)
        print(v, d)
        self.print_out(v.right, d+1)

# hovedprogram for å vise i terminalen
def main():
    tree = BinaryTree()

    for i in [5,4,6,3,7,2,8,1,9]:
        tree.insert(i, tree.root)

    tree.print_out(tree.root)
    
main()