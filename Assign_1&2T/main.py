f = open("grade.csv",'r')

mark = []

for line in f:
    line = line.split(",")
    mark.append(int(line[1]))
length = len(mark)
print(sum(mark)/length)


