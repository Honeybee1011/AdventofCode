f1 = open('input_5.txt')

rules = {}
update = []

for line in f1:
    line = line.strip()

    if '|' in line:
        line = line.split('|')
        firstPage = int(line[0])
        secPage = int(line[1])
        if firstPage not in rules:
            rules.update({firstPage:[secPage]})
        else:
            rules[firstPage].append(secPage)
    
    elif ',' in line:
        line = line.split(',')
        pages = []
        for num in line:
            pages.append(int(num))
        update.append(pages)
    
f1.close()

total = 0

for line in update:
    pastPages = []
    valid = True

    length = len(line)
    i = 0

    while i < length:
        edited = False
        if line[i] in rules:
            for k in range(i):
                if line[k] in rules[line[i]]:
                    incorrectNum = line.pop(i)
                    line.insert(k, incorrectNum)
                    i = 0
                    valid = False
                    edited = True
                    break

            if edited == True:
                i = 0
            else:
                i += 1
        else:
            i += 1
        

    if valid == False:
        middle = len(line) // 2
        total += line[middle]

print(total)