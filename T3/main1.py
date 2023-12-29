with open("text.txt","r+") as fd:
    print("Reading in r+:")
    print(fd.read())


open text.txt in w+ mode
with open("text.txt","w+") as fd:
    print("Writing in w+:")
    fd.write("New text1.")
    fd.seek(0)
    print(fd.read())

with open("text.txt","w+") as fd:
    print("Writing in w:")
    fd.write("New text1.")
    fd.seek(0)
    print(fd.read())


with open("text.txt","r+") as fd:
    print("Writing in r+:")
    fd.write("New text1.")
    fd.seek(0)
    print(fd.read())

with open("b.txt","w+") as fd:
    pass



with open("sample.txt","w+") as fd:
    print("Writing in w+:")
    fd.write("New text2")
    fd.seek(0)
    print(fd.read())

