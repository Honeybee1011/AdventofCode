l1 = []
l2 = []

totalDist = 0

f1 = open("input_1.txt")

for line in f1:
    line = line.strip().split('   ')
    l1.append(int(line[0]))
    l2.append(int(line[1]))

f1.close()

l1.sort()
l2.sort()

length = len(l1)

for i in range(length):
    dist = abs(l1[i] - l2[i])
    totalDist += dist

print(totalDist)