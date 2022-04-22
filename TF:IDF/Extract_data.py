import pymongo
from keybert import KeyBERT
cluster = pymongo.MongoClient("mongodb+srv://admin:123@cluster0.iy97i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['Tweet']
collection = db['Tweet']
results = collection.find()
all_tweets = []
for result in results:
    all_tweets.append(result['body'])
#print(all_tweets)
