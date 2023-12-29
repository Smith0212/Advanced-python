import json

def readJson(filename):
    f = open(filename,'r')
    data = json.load(f)
    return data

def writeJson(filename,data):
    f = open(filename,'w')
    json.dump(data,f)

sampledata = {
    "name" : "Swayam",
    "age" : 19,
    "dob" : '06/01/2004'
}

filename = 'file.json'
writeJson(filename,sampledata)

loaddata = readJson(filename)
print("Data in file : ",loaddata)
loaddata['age'] = 20
loaddata['name'] = "priya"

writeJson(filename,loaddata)