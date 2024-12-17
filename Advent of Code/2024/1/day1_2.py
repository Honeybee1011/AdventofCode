l1 = []
d2 = {}

simScore = 0 

f1 = open("input_1.txt")

for line in f1:
    line = line.strip().split('   ')
    l1Num = int(line[0])
    l2Num = int(line[1])

    l1.append(l1Num)

    if l2Num not in d2:
        d2.update({l2Num : 1})
    else:
        d2[l2Num] += 1

f1.close()


for i in l1:
    if i not in d2:
        continue
    else:
        sim = i * d2[i]
        simScore += sim

print(simScore)