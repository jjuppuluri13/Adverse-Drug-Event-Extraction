# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
from sqlalchemy import create_engine
conn = pg.connect("dbname=AE_Positive user=postgres password=Mypostgresql#1a")
# read postgres table into pandas dataframe
df = pd.read_sql_query('SELECT * FROM pos_table', conn)

## remove punctuation from sentences
import string
exclude = set(string.punctuation)
df.sentence.apply(lambda x: ''.join(ch for ch in x if not ch in exclude))
df.sentence = df.sentence.apply(lambda x: ''.join(ch for ch in x if not ch in exclude))

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))

## remove stopwords from sentences
def remove_stop (sent):
    word_tokens = word_tokenize(sent)
    sent2 = [w for w in word_tokens if not w in stop_words]
    sent2 = ' '.join(ch for ch in sent2)
    return sent2

df.sentence.apply(remove_stop)
df.sentence = df.sentence.apply(remove_stop)


## Stemming & Lemmatization
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
# Lemmatization Function
def lemma(sent):
    words = word_tokenize(sent)
    out_sen = [wnl.lemmatize(i,j[0].lower()) if j[0].lower() in ['a','n','v'] else wnl.lemmatize(i) for i,j in pos_tag(words)]
    out_sen = ' '.join(ch for ch in out_sen)
    return out_sen

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

# Stemming Function
def word_stem(tokens):
    stems = []
    for w in tokens:
        stems.append(ps.stem(w))
    return stems

def pstem(sent):
    tokens = word_tokenize(sent)
    fin_sen = word_stem(tokens)
    fin_sen = ' '.join(ch for ch in fin_sen)
    return fin_sen

df.sentence = df.sentence.apply(lambda x: lemma(x))
df.sentence = df.sentence.apply(lambda x: word_tokenize(x))

#####print (df.sentence)


#Word2Vec model using gensim
import gensim
from gensim.models import Word2Vec
sentences = df.sentence
model = Word2Vec(sentences, size = 300, min_count = 1)
#print(model)
words = list(model.wv.vocab)
#print(words)
#print(model['psoriatic'])


# Word2Vec Visualization
import sklearn
from sklearn.decomposition import PCA
import matplotlib
from matplotlib import pyplot
X = model[model.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
pyplot.scatter(result[:, 0], result[:, 1])
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()










