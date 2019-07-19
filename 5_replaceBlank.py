# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not s:
            return s

        li = [x for x in s]

        i = 0
        old_count = 0
        replace_count = 0
        for c in s:
            if c == ' ':
                replace_count += 1
                li.extend(["", ""])
            old_count += 1

        new_count = old_count + replace_count * 2 - 1
        old_count -= 1

        while old_count >= 0 and new_count > old_count:
            if li[old_count] == ' ':
                li[new_count] = '0'
                li[new_count - 1] = '2'
                li[new_count - 2] = '%'
                new_count -= 3
            else:
                li[new_count] = li[old_count]
                new_count -= 1
            old_count -= 1
        return ''.join(li)
                

if __name__ == '__main__':
    res = Solution().replaceSpace('hello world')
    print(res)

