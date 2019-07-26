"""
File:         candy-puzzle.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  https://www.nowcoder.com/questionTerminal/8ff3e3a14ea04c6bb3a60e2e457dafb1
"""

def process(info):
    info.sort()


if __name__ == '__main__':
    info = list(map(int, input().strip().split()))
    process(info)

