'''
# 3 https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8?tpId=13&tqId=11203&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False

        i = 0
        while True:
            if i >= len(numbers):
                return True

            if numbers[i] == i:
                i += 1
                continue
            else if numbers[i] == numbers[numbers[i]]:  # duplicated
                duplication[0] = numbers[i]
                return False
            else:
                loc = numbers[i]
                numbers[i], numbers[loc] = numbers[loc], numbers[i]


Solution().duplicated([2, 3, 1, 0, 2, 5, 3], 2])





# err 1
else if numbers[i] == numbers[numbers[i]]:  # duplicated -> elif
    pass


# err 2
if i >= len(numbers):  # not duplicated
    return True -> return False (return True if duplicated else False)

# err 3
else if numbers[i] == numbers[numbers[i]]:  # duplicated
    duplication[0] = numbers[i]
    return False -> return True  # see err 2

'''


'''
5 https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not s:
            return

        li = [x for x in s]

        old_count = 0
        replace_count = 0

        for c in li:
            old_count += 1
            if c == ' ':
                replace_count += 1
                li.extend(['', ''])

        new_count = old_count + replace_count * 2 - 1
        old_count = old_count - 1

        while old_count >= 0 and new_count > old_count:
            if li[old_count] == ' ':
                li[new_count] = '0'
                li[new_count - 1] = '2'
                li[new_count - 2] = '%'
                new_count = new_count - 3
            else:
                li[new_count] = li[old_count]
            old_count -= 1
        return ''.join(li)


Solution().replaceSpace('hello world')


# err 1
if not s:
    return -> return s  # string is immutable, need a return value

# err 2
else:
    li[new_count] = li[old_count]
    new_count -= 1  # add this line, or the order will be a mess

# err 3
for c in li: -> for c in s: (we change the list on the fly, so its length will change if there are spaces.)
    old_count += 1
    if c == ' ':
        replace_count += 1
        li.extend(['', ''])
'''


'''
18.2 https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?tpId=13&tqId=11209&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return pHead
        
        mHead = ListNode(0)
        pre = mHead
        cur = pHead
        
        while cur:
            # find a right location for cur to go if there are duplicated numbers
            # else do nothing
            inner_cur = cur
            duplicated = 0
            while inner_cur:
                if inner_cur.next:  # has next
                    if inner_cur.val == inner_cur.next.val:  # duplicated
                        inner_cur = inner_cur.next
                        duplicated += 1
                    else:  # current val is not equal to next val
                        if duplicated:  # if duplicated, go forward and break
                            inner_cur = inner_cur.next
                            break
                        else:  # no duplicated, do nothing
                            break
                else:  # the last node
                    if duplicated:  # go forward(None) and break
                        inner_cur = inner_cur.next
                        break
                    else:  # no duplicated, do nothing
                        break
                        
            # let cur to its new location
            cur = inner_cur
            
            # do nothing to cur if duplicated since we have put it to its right location
            # but don't forget let pre.next points to new cur
            if duplicated:
                pre.next = cur
            else:  # cur's location does not change, traverse the linked list in a normal way
                pre = cur
                cur = cur.next
                


# err 1
mHead = ListNode(0)
mHead.next = pHead -> forget pointing handy node to pHead
pre = mHead
cur = pHead


# err 2
return mHead.next -> forget return value
'''
