from math import gcd

f1 = open('input_8.txt')
antennaLoc = {}
grid = []

for line in f1:
    line = line.strip()
    grid.append(line)

f1.close()

height = len(grid)
width = len(grid[0])

for i in range(height):
    for j in range(width):
        point = grid[i][j]
        if point != '.':
            if point not in antennaLoc:
                antennaLoc.update({point: [[i, j]]})
            else:
                antennaLoc[point].append([i, j])
        
antinodes = []

for i in antennaLoc:
    antennas = antennaLoc[i]
    for j in range(len(antennas) - 1, 0, -1):
        for k in range(j):
            deltaRow = antennas[j][0] - antennas[k][0]
            deltaCol = antennas[j][1] - antennas[k][1]

            divisor = gcd(deltaCol, deltaRow)
                
            deltaCol = deltaCol // divisor
            deltaRow = deltaRow // divisor
            nodepointer = antennas[k]

            while True:
                if nodepointer not in antinodes:
                    antinodes.append(nodepointer)

                nodepointer = [nodepointer[0] - deltaRow, nodepointer[1] - deltaCol]

                if nodepointer[0] < 0 or nodepointer[0] >= height or nodepointer[1] < 0 or nodepointer[1] >= width:
                    break

            nodepointer = antennas[k]

            while True:
                if nodepointer not in antinodes:
                    antinodes.append(nodepointer)

                nodepointer = [nodepointer[0] + deltaRow, nodepointer[1] + deltaCol]

                if nodepointer[0] < 0 or nodepointer[0] >= height or nodepointer[1] < 0 or nodepointer[1] >= width:
                    break
            
                

print(len(antinodes))