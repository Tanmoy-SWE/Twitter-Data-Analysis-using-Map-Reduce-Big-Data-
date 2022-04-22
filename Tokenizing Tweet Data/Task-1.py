import pymongo
from keybert import KeyBERT
import csv
cluster = pymongo.MongoClient("mongodb+srv://admin:123@cluster0.iy97i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['Tweet']
collection = db['Tweet']
results = collection.find()
all_tweets = ""
for result in results:
    all_tweets = all_tweets + result['body'] + " "
   # all_tweets = all_tweets + result['body'] + " "

#print(len(all_tweets))

key_model = KeyBERT()
keywords = key_model.extract_keywords(all_tweets)
print(keywords)
with open('keywords.csv','w') as out:
    csv_out=csv.writer(out)
    for row in keywords:
        csv_out.writerow(row)
