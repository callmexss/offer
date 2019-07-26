"""
File:         words-puzzle.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  https://www.nowcoder.com/questionTerminal/8fb1e165abcb4b709d5a2f0ba759d0a6?f=discussion 
"""

def find_word_right(matrix, word, i, j, k):
    if (i >= len(matrix) or 
        j >= len(matrix[0]) or
        k >= len(word) or
        matrix[i][j] != word[k]):
        return False

    if k == len(word) - 1:
        return True

    return find_word_right(matrix, word, i, j+1, k+1) 

def find_word_down(matrix, word, i, j, k):
    if (i >= len(matrix) or 
        j >= len(matrix[0]) or
        k >= len(word) or
        matrix[i][j] != word[k]):
        return False

    if k == len(word) - 1:
        return True

    return find_word_down(matrix, word, i+1, j, k+1) 

def find_word_diagonal(matrix, word, i, j, k):
    if (i >= len(matrix) or 
        j >= len(matrix[0]) or
        k >= len(word) or
        matrix[i][j] != word[k]):
        return False

    if k == len(word) - 1:
        return True

    return find_word_diagonal(matrix, word, i+1, j+1, k+1) 
 

def process(matrix, word):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if find_word_right(matrix, word, i, j, 0):
                count += 1
            if find_word_down(matrix, word, i, j, 0):
                count += 1
            if find_word_diagonal(matrix, word, i, j, 0):
                count += 1
    print(count)


if __name__ == '__main__':
    T = int(input())  # the count of test groups
    for group_i in range(T):
        matrix = []
        row_count, col_count = list(map(int, input().split()))
        for i in range(row_count):
            matrix.append(input().strip())
        word = input().strip()
        process(matrix, word)

