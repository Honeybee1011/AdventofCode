f1 = open('input5.txt')

rules = {}
pages = []

for line in f1:
    line = line.strip()

    if '|' in line:
        line = line.split('|')
        if line[0] not in rules:
            rules.update(line[0], [line[1]])
        else:
            rules[line[0]].append(line[1])
    
    elif ',' in line:
        line = line.split(',')

        for num in line:
            pages.append(int(num))
    
f1.close()

print(rules)
print(pages)