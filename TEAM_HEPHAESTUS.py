import csv

path = str(input("Enter the file path: "))
file = open(path)
csvreader = csv.reader(file)
header = next(csvreader)
total = [header]
count = int(1)
data = []
percent = int(5)

for i in csvreader:
    data.append(i)

for row in data:
    for a in range(0, len(row)):
        for b in range(a+1, len(row)):
            if row[a] is None or row[b] is None:
                break
            i = row[a].split(" ")
            j = row[b].split(" ")
            if (len(i) == len(j) == 1) and i == j:
                row[a] = None
            elif len(j) == 1 and len(i) > 1:
                if i in j:
                    pass
            elif len(i) == 1 and len(j) > 1:
                if j in i:
                    pass
            else:
                for x in range(0, len(i)):
                    for y in range(0, len(j)):
                        if i[x] == j[y]:
                            row[a][x].translate("")
    total.append(row)
    count += 1

    if count > (len(data)/100)*percent:
        print(percent, "% addresses verified")
        percent += 5

with open(path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(total)

file.close()