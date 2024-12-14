matrix = []
with open("./input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        st = line.strip()
        matrix.append(list(st))

# DIRECTIONS = {
#     "TL": (-1,-1),
#     "T": (-1, 0),
#     "TR": (-1, 1),
#     "L": (0, -1),
#     "R": (0, 1),
#     "BL": (1,-1),
#     "B": (1, 0),
#     "BR": (1, 1)
# }

def traverse(row, col, matrix, dir, togo, sofar):
    if sofar == "XMAS":
        return 1

    if row < 0 or row > len(matrix) or col < 0 or col > len(matrix[0]):
        return 0

    try:
        hold = matrix[row][col]
    except:
        return 0
    # print("togo: ", togo)
    # print("sofar: ", sofar)
    ch = togo[0]
    count = 0
    if matrix[row][col] == ch:
        matrix[row][col] = '.'
        match dir:
            case "TL":
                # TL
                count += traverse(row-1,col-1,matrix, dir, togo[1:], sofar + ch) 
            case "T":
                # T
                count += traverse(row-1,col,matrix, dir, togo[1:], sofar + ch) 
            case "TR":
                # TR
                count += traverse(row-1,col+1,matrix, dir, togo[1:], sofar + ch) 
            case "L":
                # L
                count += traverse(row,col-1,matrix, dir, togo[1:], sofar + ch) 
            case "R":
                # R
                count += traverse(row,col+1,matrix, dir, togo[1:], sofar + ch) 
            case "BL":
                # BL
                count += traverse(row+1,col-1,matrix, dir, togo[1:], sofar + ch) 
            case "B":
                # B
                count += traverse(row+1,col,matrix, dir, togo[1:], sofar + ch) 
            case "BR":
                # BR
                count += traverse(row+1,col+1,matrix, dir, togo[1:], sofar + ch) 

        matrix[row][col] = hold
    print("count: ", count)
    return count

ans = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "X":
            ans += traverse(row, col, matrix, "TL", "XMAS", "") 
            ans += traverse(row, col, matrix, "T", "XMAS", "") 
            ans += traverse(row, col, matrix, "TR", "XMAS", "") 
            ans += traverse(row, col, matrix, "L", "XMAS", "") 
            ans += traverse(row, col, matrix, "R", "XMAS", "") 
            ans += traverse(row, col, matrix, "BL", "XMAS", "") 
            ans += traverse(row, col, matrix, "B", "XMAS", "") 
            ans += traverse(row, col, matrix, "BR", "XMAS", "") 
            print("ans:", ans)

print("final: ", ans)
