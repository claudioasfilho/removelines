import re


content = open('test.txt', 'r')
outF = open("myOutFile.txt", "w")


for line in content:
    line = re.sub('\s',' ', line)
    outF.write(line)
    #print(line)

outF = open("myOutFile.txt", "r")
outF1 = open("myOutFile1.txt", "w")

for line in outF:
    line = re.sub(r"\. ",".\n", line)
    line = re.sub(r"\-\-","", line)
    line = re.sub(r"\-"," ", line)
    #line2 = re.sub(r"\s\.(?![^(]*\))","\n",line)
    #line.replace(". ", ".\n")
    outF1.write(line)
    print(line)
