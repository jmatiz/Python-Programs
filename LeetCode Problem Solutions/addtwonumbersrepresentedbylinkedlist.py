# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      
        def convertToNumber(l1: ListNode):
            result = 0
            i = 0
            while True:
                place = 10 ** i
                result = result + (l1.val * place)
                i = i + 1
                if l1.next is not None:
                    l1 = l1.next
                else:
                    break
            return result

        l1number = convertToNumber(l1)
        l2number = convertToNumber(l2)
        
        print(l1number)
        
        print(l2number)
        
        l3number = l1number + l2number
        
        print(l3number)
            
        l3string = str(l3number)
    
        l3 = ListNode(int(l3string[-1]))
        
        head = l3
        
        for x in range(2,len(l3string)+1):
            
            head.next = ListNode(int(l3string[-x]))
            head = head.next
            
            
            
        return l3
            
    
        
