# class Solution:
#     def reverse(self, x):
#         """
#         :type x:int
#         :rtype: int
#         """
#         s = str(x)
#         length = len(s)
#         left = 0
#         right = length - 1
#         mid = (left + right) / 2
#         for i in range(length):
#             if i > mid:
#                 return int(s)
#             temp = s[i]
#             s[i] = s[-i - 1]
#             s[-i - 1] = temp
#
#
# if __name__ == '__main__':
# s = str(18)
# print(s)
# print(type(s))
# length = len(s)
# for i in range(length):
#     print(s[i])
#     print(i)
# print(int('12'))
# print(type(int('12')))
# s=str(241142)
# print(s[1])
# s = Solution()
# s.reverse(12345678)
# 一开始犯了错误 python里头string是无法更改的 所以后面用list
class Solution:
    def reverse(self, x):
        """
        :type x:int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < -2147483648 or x > 2147483647:
            return 0

        p = abs(x)
        # 先把int转化成list
        # 或者也可以用 map(int,str(num))
        l = [int(n) for n in str(p)]
        length = len(l)
        mid = (length - 1) / 2
        for i in range(length):
            if i >= mid:
                d=int(''.join(map(str, l)))
                if d < -2147483648 or d > 2147483647:
                    return 0
                if x < 0:
                    return -d
                else:
                    return d
            temp = l[i]
            l[i] = l[-i - 1]
            l[-i - 1] = temp


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1234567))
    print(s.reverse(12345678))
    print(type(-20))
    print(s.reverse(-1234))
    print(abs(0))
    d = s.reverse(1)
    print(d)
    print(int(''.join(map(str, [1]))))
    print(s.reverse(123))
    print(s.reverse(1534236469))
    print(9646324351)
