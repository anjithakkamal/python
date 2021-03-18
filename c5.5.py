f = open("D:/20mca/python file/pyfile.csv", "a")
import json
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open("D:/20mca/python file/pyfile.csv", "r")
print(f.read())