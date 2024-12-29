with open("./input.txt", "r") as f:
    lines = f.readlines()

lists = []
for line in lines:
    st = line.strip()
    sp = list(map(int, st.split()))
    lists.append(sp)

safe = 0
for li in lists:
    dir = "pos"
    if li[1] < li[0]:
        dir = "neg"
    ok = True
    for l in range(1, len(li)):
        if dir == "pos" and li[l] > li[l - 1]:
            diff = li[l] - li[l - 1]
            if diff > 3 or diff < 1:
                if ok:
                    ok = False
                    pass
                else:
                    break
        elif dir == "neg" and li[l] < li[l - 1]:
            diff = li[l - 1] - li[l]
            if diff > 3 or diff < 1:
                if ok:
                    ok = False
                    pass
                else:
                    break
        else:
            if ok:
                ok = False
                pass
            else:
                break

        if l == len(li) - 1:
            print(li)
            print(dir)
            print(li[l])
            safe += 1

print(safe)
