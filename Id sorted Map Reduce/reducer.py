from mapper import mapperId

myfile = open('reducerOutput.txt', 'a')
i = 0
for j in range(0,len(mapperId)):
    i = j + 1
    cnt = 1
    while (i != 0):
        i = i - 1
        if mapperId[j][0] == mapperId[i][0]:
            cnt = cnt - 1
            break
    for j in range(i + 1, len(mapperId)):
        if (mapperId[j][0] == mapperId[i][0]):
            cnt = cnt + 1
    if cnt > 0:
        myfile.write(mapperId[j][0] + " " + (str)(cnt) + "\n")

myfile.close()