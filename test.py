import json
a={"name": "shalini","course":"btech", "age": 20 }
out_file = open("rc.json", "w")

json.dump(a, out_file,indent=12)

out_file.close() 
