class Node:
    def __init__ (self, dataval = None):
        self.dataval = dataval
        self.nextval = None
        self.prevval = None

class slinkedlist:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def atbeginning(self,newdata):
        new_node = Node(newdata)
        new_node.nextval = self.headval
        if self.headval is not None:
            self.headval.prevval = new_node
        self.headval = new_node
        
    def atend(self,newdata):
        new_node = Node(newdata)
        if self.headval is None:
            new_node.prevval = None
            self.headval = new_node
            return
        lastnode = self.headval
        while lastnode.nextval is not None:
            lastnode = lastnode.nextval
        lastnode.nextval = new_node
        new_node.prevval = lastnode
        
    def atnode(self,newdata,atnode):
        if atnode is None:
            print("That node does not exist")
            return
        new_node = Node(newdata)

        new_node.nextval = atnode.nextval
        atnode.nextval.prevval = new_node
        atnode.nextval = new_node
        new_node.prevval = atnode
        
            
    def delnode(self,target_data):

        head = self.headval

        if head is not None:
            if head.dataval == target_data:
                self.headval = head.nextval
                self.headval.prevval = None
                head = None
                return
        while head is not None:
            if head.dataval == target_data:
                break
            previous = head
            head = head.nextval
        if head is not None:
            previous.nextval = head.nextval
            head.nextval.prevval = previous

        head = None
            

list1 = slinkedlist()

list1.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

list1.headval.nextval = e2

e2.nextval = e3



list1.atbeginning("Sun")

list1.listprint()

list1.atend("thurs")

list1.listprint()

list1.atnode("mondaynight", list1.headval.nextval)
list1.listprint()

list1.delnode("mondaynight")
print("testing delete")

list1.listprint()
