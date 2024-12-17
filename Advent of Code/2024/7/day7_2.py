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
        

        numLen = len(str(l[0])) * -1

        if str(val)[numLen:] == str(l[0]):
            if val == l[0]:
                l = l[1:]
                for i in l:
                    if i != 1:
                        return False
                return True
            
            if val % l[0] == 0:
                return deconstruct(l[1:], int(str(val)[:numLen])) or (deconstruct(l[1:], val // l[0]) or deconstruct(l[1:], val - l[0]))
            if val - l[0] >= 0:
                return deconstruct(l[1:], val - l[0]) or deconstruct(l[1:], int(str(val)[:numLen]))

        if val % l[0] == 0:
            return deconstruct(l[1:], val // l[0]) or deconstruct(l[1:], val - l[0])
        
        if val - l[0] >= 0:
            return deconstruct(l[1:], val - l[0])
        

    if deconstruct(equation, testValue):
        counter += testValue
        

f1.close()

print(counter)

#227916904994235 too low
#227921760109726