#from Extract_data import id
from mergeSort import sortedId
myfile = open('mapperOutput.txt', 'a')
mapperId = []
for i in range(0, len(sortedId)):
    myfile.write((str)(sortedId[i])+" 1\n")
myfile.close()