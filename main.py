list = []
n = int(input())
for i in range(n):
    list.append(int(input()))
    list2 = list[i] ** 2

print(*list2)