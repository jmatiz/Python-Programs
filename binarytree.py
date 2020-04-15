class Node:
    def __init__(self, data):
        self.data = data
        self.leftnode = None
        self.rightnode = None

    def insertNode(self, insertdata):
        if insertdata < self.data:
            if self.leftnode is None:
                self.leftnode = Node(insertdata)
            else:
                self.leftnode.insertNode(insertdata)
        elif insertdata > self.data:
            if self.rightnode is None:
                self.rightnode = Node(insertdata)
            else:
                self.rightnode.insertNode(insertdata)
        else:
            self.data = insertdata
                
            
            


    def printTree(self): #inorder
        if self.leftnode is not None:
            self.leftnode.printTree()
        print(self.data)
        if self.rightnode is not None:
            self.rightnode.printTree()
      
        
    def preorder(self):
        print(self.data)
        if self.leftnode is not None:
            self.leftnode.preorder()
        if self.rightnode is not None:
            self.rightnode.preorder()

    def search(self, searchdata):
        if self.data is not None:
            if searchdata < self.data:
                if self.leftnode is not None:
                    self.leftnode.search(searchdata)
                else:
                    print(str(searchdata) + " is not found in this tree")
                    return
            elif searchdata > self.data:
                if self.rightnode is not None:
                    self.rightnode.search(searchdata)
                else:
                    print(str(searchdata) + " is not found in this tree")
                    return
            else: #searchdata == self.data
                print(str(searchdata) + " is found in this tree")
                return

        else:
            print("There is nothing in this tree")
            return



BST = Node(10)

BST.insertNode(12)

BST.insertNode(8)

BST.insertNode(3)

BST.insertNode(1)

BST.insertNode(6)

BST.insertNode(11)

BST.printTree()

BST.search(7)

