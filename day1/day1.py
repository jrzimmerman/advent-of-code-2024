lines = []
with open("./input.txt", "r") as f:
    lines = f.readlines()

count = 0
left = []
right = []
for line in lines:
    st = line.strip()
    # print(st)
    sp = st.split()
    # print(sp)

    left.append(int(sp[0]))
    right.append(int(sp[1]))

left = sorted(left)
right = sorted(right)
for i in range(len(left)):
    l = left[i]
    r = right[i]
    count += abs(r - l)
# print(count)

map = {}

for j in range(len(left)):
    map[left[j]] = 0

print(map)

for k in range(len(right)):
    print(right[k])
    if right[k] in map:
        map[right[k]] += 1

ans = 0
for key in map:
    ans += key * map[key]
print(ans)
