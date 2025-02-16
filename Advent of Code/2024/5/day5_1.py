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

    for page in line:
        if page in rules:
            for past in pastPages:
                if past in rules[page]:
                    valid = False

        pastPages.append(page)

    if valid == True:
        middle = len(line) // 2
        total += line[middle]

print(total)