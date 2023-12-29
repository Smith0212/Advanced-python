with open("read.txt", "r") as f:
    que = f.readlines()

for line in que:
    line = line.split()
    if line[len(line)-1].endswith("?"):
        line = " ".join(line)
        print(f"Question : {line}")
    else:
        line = " ".join(line)
        print(f"Option: {line}")