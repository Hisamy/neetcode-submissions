# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        
        # Ambos punteros inician en la zona segura (el dummy)
        current = dummy
        tail = dummy
        
        # 1. Separamos 'tail' exactamente 'n' pasos
        for i in range(n):
            tail = tail.next
            
        # 2. Avanzamos ambos simultáneamente de forma segura
        while tail.next:
            current = current.next
            tail = tail.next
            
        # 3. Saltamos el nodo objetivo
        current.next = current.next.next
        
        return dummy.next









            

        