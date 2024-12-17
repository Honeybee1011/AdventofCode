# totalSafe = 0
# listReports = []

# f1 = open("input_2.txt")

# for line in f1:
#     report = []
#     line = line.strip().split(' ')

#     for level in line:
#         report.append(int(level))

#     listReports.append(report)

# f1.close()

# def gapChecker(list): #Checks the gaps in between the values. Assume values are in order
#     for i in range(len(list) - 1):
#         diff = abs(list[i+1] - list[i])
#         if diff > 3 or diff < 1:
#             return False
#     return True

# totalSafe = 0

# for report in listReports:
#     length = len(report)

#     prev = report[1] - report[0]
#     changeCount = 1

#     for i in range(length - 1): 
#         diff = report[i+1] - report[i]
#         if prev * diff < 0:
#             changeCount += 1
#         prev = diff

#     if changeCount > 3:
#         continue

#     #Make something that can check if the record is valid if one point is removed

#     for i in range(length - 1):
#         testReport = report[:i] + report[i+1:]
#         print(testReport)
#         if gapChecker(testReport):
#             totalSafe += 1
#             break

# print(totalSafe)

totalSafe = 0
listReports = []

f1 = open("input_2.txt")

for line in f1:
    report = []
    line = line.strip().split(' ')

    for level in line:
        report.append(int(level))

    listReports.append(report)

f1.close()

totalSafe = 0

for report in listReports:
    length = len(report)

    for level in range(length):
        testReport = report[:level] + report[level+1:]
        valid = True
        
        if testReport[0] < testReport[1]: 
            for i in range(length - 2):
                diff = testReport[i+1] - testReport[i]
                if diff > 3 or diff < 1:
                    valid = False

        else:
            for i in range(length - 2):
                diff = testReport[i] - testReport[i+1]
                if diff > 3 or diff < 1:
                    valid = False
                    
        if valid == True:
            totalSafe += 1
            break


print(totalSafe)