# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1:ListNode
        :type l2:ListNode
        :rtype: ListNode
        """
        # if l1 == None:
        #     return l2
        # if l2 == None:
        #     return l1
        ans=ListNode(0)
        temp=ans
        tempsum=0
        while True:
            if (l1!=None):
                tempsum=l1.val+tempsum
                l1=l1.next
            if (l2!=None):
                tempsum=l2.val+tempsum

            temp.val=tempsum%10
            tempsum=int(tempsum/10)
            if l1==None and 12==None and tempsum==0:
                break
            temp.next=ListNode(0)
            temp=temp.next
        return ans






if __name__ == '__main__':
    if __name__ == '__main__':
        # 创建对象Solution
        sol = Solution()
        # 定义l1链表
        l1 = ListNode(2)
        l1.next = l11 = ListNode(4)
        l11.next = l12 = ListNode(5)
        # 定义l2链表
        l2 = ListNode(5)
        l2.next = l21 = ListNode(6)
        l21.next = l22 = ListNode(4)
        # 获取返回值的链表
        res = sol.addTwoNumbers(l1, l2)
        # 循环遍历出来
        while res:
            print(res.val)
            res = res.next