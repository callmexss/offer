"""
File:         a-strange-letter.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  https://www.nowcoder.com/practice/d7764905e41a413c98900e22a9cc4ec3?tpId=98&&tqId=32893&rp=1&ru=/activity/oj&qru=/ta/2019test/question-ranking
"""
def process(s, width_li):
    '''Process the lines of this input stram.'''
    lines = 0
    count = 0
    line_width = 100
    for c in s:
        index = ord(c) - ord('a')
        if count + width_li[index] > line_width:
            lines += 1
            count = width_li[index]
        else:
            count += width_li[index]
    lines = lines + 1 if count > 0 else lines
    print(lines, count)


if __name__ == '__main__':
    width_li = list(map(int, input().strip().split()))
    s = input().strip()
    
    if not width_li or not s:
        exit()
    
    process(s, width_li)

