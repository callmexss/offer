import dis


for i in range(10):
    if i == 5:
        break

print(i)  # 5



li = [1, 2, 3, 4, 5]
print(li)
li[0], li[li[0]] = li[li[0]], li[0]
print(li)

