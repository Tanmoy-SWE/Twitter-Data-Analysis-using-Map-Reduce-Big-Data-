import pymongo
from keybert import KeyBERT
cluster = pymongo.MongoClient("mongodb+srv://admin:123@cluster0.iy97i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['Tweet']
collection = db['Tweet']
results = collection.find()
tweet_cities = []
for result in results:
    try:
        #print(result['actor']['location'])
        text = result['actor']['location']['displayName']
        if 'Australia' in text:
            tweet_cities.append((str)(result['actor']['twitterTimeZone']))
    except:
        pass
print(tweet_cities)