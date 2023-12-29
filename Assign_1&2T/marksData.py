def readCsv(fileName):
    f = open(fileName,"r")
    data = []
    for line in f:
        line = line.strip()
        for i in line: 
            line = line.split(",")
            data.append(int(line))

    return data

def calculateCsv(list_data):
    x = []
    count = 0
    for i in list_data:
        for j in i:
            s = int(list_data[i][j])
            x.append(s)
            count +=1

    total = sum(x)
    avg = total/count
    return avg



mylist = readCsv("marksdata.csv")
print(calculateCsv(mylist))
print(list)
result= 0
for i in list:
    for j in i:
        result = result + list[j]

print(sum)
