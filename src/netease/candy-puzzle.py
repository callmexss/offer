"""
File:         candy-puzzle.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  https://www.nowcoder.com/questionTerminal/8ff3e3a14ea04c6bb3a60e2e457dafb1
"""
def process(info):
    info.sort()
    count = 0
    m = dict(zip(info, [0]*len(info)))
    for each in info:
        m[each] += 1
    res = 0
    for each in m.items():
        val, num = each
        while num > val:
            res += val + 1
            num = num - val - 1
        if num == 0:
            continue
        else:
            res += (val+1)
    print(res)


if __name__ == '__main__':
    info = list(map(int, input().split()))
    process(info)

