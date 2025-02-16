f1 = open('input_4.txt')

box1 = []

for line in f1:
    line = line.strip()
    box1.append(line)

f1.close()


total = 0
width = len(box1[0])
height = len(box1)


for j in range(1, len(box1)-1): #Iterate row
    line = box1[j]

    if j + 1 <= height:

        for k in range(1, width-1): #Iterate column
            if line[k] == 'A':

                topleft = box1[j-1][k-1]
                topright = box1[j-1][k+1]
                botleft = box1[j+1][k-1]
                botright = box1[j+1][k+1]

                if topleft == topright == 'M':
                    if botleft == botright == 'S':
                        total += 1
                
                if topleft == botleft == 'M':
                    if topright == botright == 'S':
                        total += 1

                if topleft == topright == 'S':
                    if botleft == botright == 'M':
                        total += 1
                
                if topleft == botleft == 'S':
                    if topright == botright == 'M':
                        total += 1


print(total)