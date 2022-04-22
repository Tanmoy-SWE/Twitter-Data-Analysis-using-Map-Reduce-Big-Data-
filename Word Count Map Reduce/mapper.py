import sys
result = ""
f = open('tweets.txt','r')
line = f.read()
word = line.split()
myfile = open('mapperOutput.txt', 'a')
for i in word:
        temp = i+" "+(str)(1)+"\n"
        myfile.write(temp)
myfile.close()