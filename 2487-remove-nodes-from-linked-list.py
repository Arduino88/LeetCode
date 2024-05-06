def insertAtEnd(head, data):
    new_node = ListNode(data)
 
    current_node = head
    while(current_node.next):
        current_node = current_node.next
 
    current_node.next = new_node


def isValid(node) -> bool:
    if node.next is None:
        return True
    
    tempNode = node
    while tempNode is not None:
        if tempNode.val > node.val:
            return False
        tempNode = tempNode.next

    return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        returnHead = ListNode
        returnHead.val = None
        returnHead.next = None
        node = head
        while node is not None:
            #print(node.val, isValid(node))
            if isValid(node):
                insertAtEnd(returnHead, node.val)

            node = node.next

        returnHead = returnHead.next
        return returnHead