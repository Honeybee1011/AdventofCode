total = 0

f1 = open('input_3.txt')


for line in f1:
    i = 0
    line = line.strip()

    while i < len(line):
        start = line[i:i+4]
        if start == 'mul(':
            j = i+4
            num1 = ''
            num2 = ''

            while line[j].isdigit() and j < i+7:
                num1 += line[j]
                j += 1
            
            if line[j] != ',':
                i += 1
                continue
            
            j += 1

            while line[j].isdigit() and j < i+11:
                num2 += line[j]
                j += 1

            if line[j] != ')':
                i += 1
                continue


            print(num1, num2)
            prod = int(num1) * int(num2)
            
            total += prod
            
        i += 1

print(total)
f1.close()