room = []
guardStart = []
obstacles = []
placements = 0

f1 = open('input_6.txt')

for line in f1:
    line = line.strip()
    room.append(line)

f1.close()

dir = 'w' #wasd controls

height = len(room)
width = len(room[0])


for i in range(height):
    for j in range(width):
        if room[i][j] == '^':
            guardStart = [i, j]
        
        if room[i][j] == '#':
            obstacles.append([i, j])

for i in range(height):
    for j in range(width):
        if [i, j] == guardStart:
            continue
        dir = 'w'
        guard = guardStart[:]
        passed = {tuple(guardStart[:]): 1}
        newObstacles = obstacles[:]
        newObstacles.append([i, j])
        print([i, j])

        while True:
            nextStep = guard[:]
            if dir == 'w':
                nextStep[0] -= 1

            elif dir == 'd':
                nextStep[1] += 1

            elif dir == 's':
                nextStep[0] += 1
            
            elif dir == 'a':
                nextStep[1] -= 1

            if nextStep[0] < 0 or nextStep[1] < 0 or nextStep[0] >= height or nextStep[1] >= width:
                break

            if nextStep in newObstacles:
                if dir == 'w':
                    dir = 'd'
                elif dir == 'd':
                    dir = 's'
                elif dir == 's':
                    dir = 'a'
                elif dir == 'a':
                    dir = 'w'
                continue
            
            nextStepTup = tuple(nextStep[:])

            if nextStepTup not in passed:
                passed.update({nextStepTup:1})
            else:
                if passed[nextStepTup] < 5:
                    passed[nextStepTup] += 1
                else:
                    placements += 1
                    print("it's working")
                    break
                    

            guard = nextStep

print(placements)
#1448 too high