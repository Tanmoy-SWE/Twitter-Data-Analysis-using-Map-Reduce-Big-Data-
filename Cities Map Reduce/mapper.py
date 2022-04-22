from Extract_data import tweet_cities
myfile = open('mapperOutput.txt', 'a')
for i in range(0, len(tweet_cities)):
    myfile.write(tweet_cities[i]+"  "+(str)(1))
myfile.close()