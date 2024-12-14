import re

with open("./input.txt", "r") as f:
    lines = f.readlines()

enabled = True
ans = 0
for line in lines:
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", line)
    print(matches)
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        else:
            if enabled:
                # print(match)
                m = re.findall(r"\d+", match)
                # print(m)
                ans += int(m[0]) * int(m[1])
print(ans)
