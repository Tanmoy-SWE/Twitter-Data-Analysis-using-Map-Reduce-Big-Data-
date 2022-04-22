from Extract_data import tweet_cities

myfile = open('reducerOutput.txt', 'a')
i = 0
for city in range(0,len(tweet_cities)):
    i = city + 1
    cnt = 1
    while (i != 0):
        i = i - 1
        if tweet_cities[city] == tweet_cities[i]:
            cnt = cnt - 1
            break
    for j in range(i + 1, len(tweet_cities)):
        if (tweet_cities[city] == tweet_cities[i]):
            cnt = cnt + 1
    if cnt > 0:
        myfile.write(tweet_cities[city] + " " + (str)(cnt) + "\n")

myfile.close()