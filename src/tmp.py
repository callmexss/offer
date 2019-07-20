import dis


if __name__ == "__main__":
    for i in range(10):
        if i == 5:
            break

    print(i)  # 5


    li = [1, 2, 3, 4, 5]
    print(li)
    li[0], li[li[0]] = li[li[0]], li[0]
    print(li)


    li = [x for x in range(1, 13)]
    it = iter(li)
    rows = 3
    cols = 4
    print([[next(it) for i in range(rows)] for j in range(cols)])
