counter = 0

f1 = open('input_7.txt')


for line in f1:
    line = line.strip()

    separater = line.index(':')
    testValue = int(line[:separater])
    equation = []

    for i in line[separater+1:].strip().split():
        equation.append(int(i))

    equation = equation[::-1]

    def deconstruct(l, val):
        if len(l) == 1:
            return l[0] == val
        
        if val % l[0] == 0:
            return deconstruct(l[1:], val // l[0]) or deconstruct(l[1:], val - l[0])
        
        if val - l[0] >= 0:
            return deconstruct(l[1:], val - l[0])
        

    if deconstruct(equation, testValue):
        counter += testValue
        

f1.close()

print(counter)
#241 too low
#410 too low
#500 wrong