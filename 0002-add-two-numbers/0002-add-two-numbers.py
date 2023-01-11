# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def helper(l1, l2, carry):
            if l1 == None and l2 == None: 
                if carry == 0:
                    return None
                else:
                    return ListNode(1)
            if l1 == None:
                l1 = ListNode()
            elif l2 == None:
                l2 = ListNode()
            tmpsum = l1.val + l2.val + carry
            
            if tmpsum < 10:
                res = helper(l1.next, l2.next, 0)  
                return ListNode(tmpsum, res)
            else:
                res = helper(l1.next, l2.next, 1)  
                return ListNode(tmpsum % 10, res)
            
        return helper(l1, l2, 0)
                
        
        ''' dumb 
        def helper(l1, l2):
            if l1 == None and l2 == None:
                return None, 0
            if l1 == None:
                l1 = ListNode()
            elif l2 == None:
                l2 = ListNode()
                
            res, carry = helper(l1.next, l2.next)              
            tmpsum = l1.val + l2.val + carry
            
            if tmpsum < 10:
                return ListNode(tmpsum, res), 0
            else:
                return ListNode(tmpsum % 10, res), 1
                
        res, carry = helper(l1, l2)
        if carry == 1:
            return ListNode(1, res)
        else:
            return res
        '''