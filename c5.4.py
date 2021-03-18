import csv
with open('D:/20mca/python file/pyfile.csv', 'r',) as file:
 reader = csv.reader(file)
 for row in reader:
     print(row)