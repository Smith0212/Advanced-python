def readCsv(fileName):
    f = open(fileName,'r')
    mylist = []
    for line in f:
        line = line.split(",")
        mylist.append(int(line[1]))
        return mylist

def avgMarks(data_list):
    length = len(data_list)
    avg = sum(data_list)/length
    return avg


# main

marks_list = readCsv("/Users/swayampalrecha/Desktop/class theory pythonn/second week/third program/file.csv")
print(avgMarks(marks_list))
