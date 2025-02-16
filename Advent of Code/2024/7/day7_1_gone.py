counter = 0

f1 = open('input_7.txt')


for line in f1:
    line = line.strip()

    separater = line.index(':')
    testValue = int(line[:separater])
    equation = []

    for i in line[separater+1:].strip().split():
        equation.append(int(i))

    numTests = 2 ** (len(equation) - 1)

    for i in range(numTests):
        tester = equation[0]
        binary = bin(i)
        binary = binary[2:]
        binary = binary.zfill(len(equation)-1)

        for j in range(len(binary)): #Let 0 be sum and 1 be product
            if binary[j] == '0':
                tester *= equation[j+1]
            else:
                tester += equation[j+1]


        if tester == testValue:
            counter += testValue
            break

f1.close()

print(counter)
#241 too low
#410 too low