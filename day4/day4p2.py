matrix = []
with open("./input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        st = line.strip()
        matrix.append(list(st))


def traverse(row, col, matrix):
    C = matrix[row][col]
    TL = matrix[row - 1][col - 1]
    TR = matrix[row - 1][col + 1]
    BL = matrix[row + 1][col - 1]
    BR = matrix[row + 1][col + 1]

    found_tr_to_bl = C == "A" and (TR == "S" and BL == "M") or (TR == "M" and BL == "S")
    found_tl_to_br = C == "A" and (TL == "S" and BR == "M") or (TL == "M" and BR == "S")

    if found_tr_to_bl and found_tl_to_br:
        return 1
    else:
        return 0


ans = 0
for row in range(1, len(matrix) - 1):
    for col in range(1, len(matrix[row]) - 1):
        if matrix[row][col] == "A":
            ans += traverse(row, col, matrix)
            print("ans:", ans)

print("final: ", ans)
