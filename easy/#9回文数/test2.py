class Solution:
    def isPalindrome(self,n):
        return str(n)==str(n)[-1::-1]