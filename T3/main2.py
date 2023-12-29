f = open("data.csv","r")

sumdi = 0
mylist = []
for line in f:
    
    line = line.split(",")
    try:
        x = int(line[0])
        mylist.append(line[0])
        sumdi = sumdi + x
       
    except ValueError:
        print(line[0] +" is not a integer type")


    

# print(sum(mylist))
print(sumdi)
    # print(int(line[0]))

    # if (line[0] == int()):
    #     sum = sum + line[0]
    # else:
    #     print("Value is not a integer type")


