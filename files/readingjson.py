import json

path = "/Users/harsh/Documents/GitHub-Harsh/python-programming/files/demo_data.json"

data = {
    "ID" : 7,
    "Name" : "Nisha",
    "Age" : 34,
    "Department" : "IT",
    "Salary" : 60000,
    "Joining Date" : "2022-06-14T00:00:00.000"
    }

def readJson(file):
    with open(path, 'r') as f:
       return json.load(f)
        

def readValues(file):
    data = readJson(file)
    for element in data:
        print(element["ID"], element["Name"], element["Age"], element["Department"],element["Salary"], element["Joining Date"])

def writeValues(newData, file):
    data = readJson(file)
    print("Before Updating")
    print(data)
    if isinstance(data, list):
        data.append(newData)
    
    with open(path, 'w') as f:
        json.dump(data, f, indent =4)
    
    print("Updatd Json Data: ")
    readValues(file)


# readJson(path)
# readValues(path)
# writeValues(data, path)




