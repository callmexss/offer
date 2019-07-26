"""
File:         bad-clock.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  https://www.nowcoder.com/questionTerminal/72f3cc4658024d12bcc122c29b35394e
"""
def process(case):
    '''Modify time to valid value.
 
    case: list, ['1', '9', ':', '0', '0', ':', '2', '3']
                ['2', '8', ':', '1', '9', ':', '9', '7']
                ['3', '8', ':', '9', '9', ':', '9', '7']
    '''
 
    if case[0] == '2':
        if case[1] > '3':
            case[0] = '0'
    if case[0] > '2':
        case[0] = '0'
    if case[3] > '5':
        case[3] = '0'
    if case[6] > '5':
        case[6] = '0'
 
 
if __name__ == '__main__':
    case_count = int(input())
    for i in range(case_count):
        case = [x for x in input().strip()]
        process(case)
        print(''.join(case))

