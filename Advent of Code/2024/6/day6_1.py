room = []
guard = []
obstacles = []
passed = []

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
            guard = [i, j]
        
        if room [i][j] == '#':
            obstacles.append([i, j])

passed.append(guard[:])

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

    if nextStep in obstacles:
        if dir == 'w':
            dir = 'd'
        elif dir == 'd':
            dir = 's'
        elif dir == 's':
            dir = 'a'
        elif dir == 'a':
            dir = 'w'
        continue

    if nextStep not in passed:
        passed.append(nextStep[:])

    guard = nextStep

print(len(passed))