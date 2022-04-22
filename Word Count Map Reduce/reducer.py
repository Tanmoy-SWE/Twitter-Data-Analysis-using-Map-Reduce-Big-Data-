import sys
result = ""
f = open('tweets.txt','r')
line = f.read()
words = line.split()
myfile = open('reducerOutput.txt', 'a')

ans = []
for word in words:
    ans.append(word.lower())

reducer = []
count = []
for i in range(0,len(ans)):
    j = i
    cnt = 1
    while(j!=0):
        j = j-1
        if ans[i]==ans[j]:
            cnt = cnt - 1
            break
    for j in range(i+1, len(words)):
        if(ans[i]==ans[j]):
            cnt = cnt + 1
    if cnt > 0:
        myfile.write(ans[i] + " "+ (str)(cnt)+"\n")
myfile.close()
