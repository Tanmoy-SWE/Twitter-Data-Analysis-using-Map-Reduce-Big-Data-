from Extract_data import all_tweets
from sklearn.feature_extraction.text import TfidfVectorizer


# merge documents into a single corpus

# create object
tfidf = TfidfVectorizer()

# get tf-df values
result = tfidf.fit_transform(all_tweets)

# get indexing
print('\nWord index:')
print(tfidf.vocabulary_['health'])

voc_index = tfidf.vocabulary_['health']


with open('output.txt', 'w') as fh:
    fh.write("Data for tf of \health'\'")
    for doc_no, num in enumerate(result.toarray()[:,voc_index]):
        fh.write(f'Tweet {doc_no} : {num}\n')
