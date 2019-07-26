"""
File:         session-list.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  https://www.nowcoder.com/practice/0f52adb3946249f9bb63d964658b2691?tpId=98&&tqId=32891&rp=1&ru=/activity/oj&qru=/ta/2019test/question-ranking
"""
from collections import deque

def process(id_li):
    has_seen = set()
    q = deque()
    output = []
    for each_id in id_li:
        if not each_id in has_seen:
            has_seen.add(each_id)
            q.appendleft(each_id)
        else:
            q.remove(each_id)
            q.appendleft(each_id)
    while q:
        output.append(q.popleft())
    outputs.append(output)


if __name__ == '__main__':
    T = int(input().strip())
    outputs = []
    for group_i in range(T):
        N = int(input().strip())
        id_li = input().split()
        process(id_li)

    for output in outputs:
        print(' '.join(output))

