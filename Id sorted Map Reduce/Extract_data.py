import pymongo
import re
from keybert import KeyBERT
cluster = pymongo.MongoClient("mongodb+srv://admin:123@cluster0.iy97i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['Tweet']
collection = db['Tweet']
results = collection.find()
id = []
for result in results:
    temp = result['object']['id']
    x = temp.split(':')
    id.append([(int)(x[2])])
print(id)
