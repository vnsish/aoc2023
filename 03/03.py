import re

def check_adjacent(row, span, mat):
    symbols = ['*', '&', '$', '@', '/', '+', '-', '#', '%', '=']
    
    for pos in range(span[0], span[1]):
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx==0 and dy==0: continue
                elif (row+dx > 0 and pos+dy > 0) and (row+dx < len(mat) and pos+dy < len(mat)):
                    if mat[row+dx][pos+dy] in symbols:
                        return True
    
    return False

def partone(input):
    mat = []
    sum = 0

    with open(input, 'r') as fp:
        for line in fp.read().split():
            mat.append(line)
    
    for i,line in enumerate(mat):
        matches = re.finditer(r'\d+', line)
        for match in matches:
            if check_adjacent(i, match.span(), mat):
                sum += int(match.group())

    print(sum)

def check_gear(pos, mat, pnums, pnum_map):
    found = []
    
    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx==0 and dy==0: continue
            elif (pos[0]+dx >= 0 and pos[1]+dy >= 0) and (pos[0]+dx < len(mat) and pos[1]+dy < len(mat)):
                if pnum_map[pos[0]+dx][pos[1]+dy] > 0 and pnum_map[pos[0]+dx][pos[1]+dy] not in found:
                    found.append(pnum_map[pos[0]+dx][pos[1]+dy])
    
    if len(found) == 2:
        return int(pnums[found[0]-1][2])*int(pnums[found[1]-1][2])
    
    return 0

def parttwo(input):
    mat = []
    sum = 0
    with open(input, 'r') as fp:
        for line in fp.read().split():
            mat.append(line)

    pnums = []        
    pnum_map = []

    for i,line in enumerate(mat):
        pnum_map.append([])
        for _ in range(len(mat)):
            pnum_map[i].append(0)
        matches = re.finditer(r'\d+', line)
        for match in matches:
            pnums.append([i, match.span(), match.group()])

    for i,pnum in enumerate(pnums):
        for j in range(pnum[1][0], pnum[1][1]):
            pnum_map[pnum[0]][j] = i+1

    for i,line in enumerate(mat):
        for j,char in enumerate(line):
            if char == '*':
                sum += check_gear((i, j), mat, pnums, pnum_map)

    print(sum)

partone('input')
parttwo('input')