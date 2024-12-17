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

totalSafe = len(listReports)

for report in listReports:
    length = len(report)

    if report[0] < report[1]:
        for i in range(length - 1):
            diff = report[i+1] - report[i]
            if diff > 3 or diff < 1:
                totalSafe -= 1
                break

    else:
        for i in range(length - 1):
            diff = report[i] - report[i+1]
            if diff > 3 or diff < 1:
                totalSafe -= 1
                break


print(totalSafe)