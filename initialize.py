import json
f = open("data/groupdata.txt","r")
line = f.readline()
data = json.loads(line)
# for dic in data:
#     print(dic["@key"])