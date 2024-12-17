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
            
            if deltaCol > 0:
                if antennas[k][0] - deltaRow >= 0 and antennas[k][1] - deltaCol >= 0:
                    antinode = [antennas[k][0] - deltaRow, antennas[k][1] - deltaCol]
                    if antinode not in antinodes:
                        antinodes.append(antinode)
                
                if antennas[j][0] + deltaRow < height and antennas[j][1] + deltaCol < width:
                    antinode = [antennas[j][0] + deltaRow, antennas[j][1] + deltaCol]
                    if antinode not in antinodes:
                        antinodes.append(antinode)
            else:
                if antennas[k][0] - deltaRow >= 0 and antennas[k][1] - deltaCol < width:
                    antinode = [antennas[k][0] - deltaRow, antennas[k][1] - deltaCol]
                    if antinode not in antinodes:
                        antinodes.append(antinode)
                
                if antennas[j][0] + deltaRow < height and antennas[j][1] + deltaCol >= 0:
                    antinode = [antennas[j][0] + deltaRow, antennas[j][1] + deltaCol]
                    if antinode not in antinodes:
                        antinodes.append(antinode)

print(len(antinodes))

#360 too high