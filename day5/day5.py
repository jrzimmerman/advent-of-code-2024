with open("./test.txt", "r") as f:
    lines = f.readlines()

lis = []
for line in lines:
    st = line.strip()
    lis.append(st)

split = 0
for i in range(len(lis)):
    if lis[i] == "":
        split = i
        break

ordering = lis[0:split]
updates = lis[split + 1 :]
print(ordering)
print(updates)

map = {}
for order in ordering:
    x, y = order.split("|")
    x, y = int(x), int(y)
    map[y] = set()
    map[y].add(x)

print(map)
