f1 = open('input_4.txt')

box1 = []

for line in f1:
    line = line.strip()
    box1.append(line)

f1.close()

def horizontal_checker(s):
    return s.count('XMAS')

def rotate(box):
    height = len(box[0])
    newBox = [''] * height

    for row in box:
        temp_row = row[::-1]

        for i in range(height):
            if newBox[i] == None:
                newBox[i] = temp_row[i]
            else:
                newBox[i] += temp_row[i]
    
    return newBox


total = 0
width = len(box1[0])
height = len(box1)

for i in range(4):
    for j in range(len(box1)): #Iterate row
        line = box1[j]
        total += horizontal_checker(line)
        
        if j + 4 <= height:

            for k in range(width-3): #Iterate column

                word = box1[j][k] + box1[j+1][k+1] + box1[j+2][k+2] + box1[j+3][k+3]

                if word == 'XMAS':
                    total += 1
        
    box1 = rotate(box1)



print(total)