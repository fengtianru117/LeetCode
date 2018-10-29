class Solution:
    def isPalindrome(self,x):
        """
        :type x: int
        :rtype: bool
        """
        d=str(x)
        if x < 0 or d[-1]==0:
            return False
        length=len(d)
        for i in range(length):
            if not d[i]==d[-i-1]:
                return False
        return True

if __name__ == '__main__':
    print(2994%10)