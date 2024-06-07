import csv 
f = open("marks.csv", "r")
r = csv.reader(f, delimiter = ":")
for row in r:
    print(row)
f.close()    
