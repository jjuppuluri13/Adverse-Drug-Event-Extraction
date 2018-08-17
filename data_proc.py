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


## remove punctuation from sentences & drugs, replace with spaces
import string
translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
df.sentence = df.sentence.apply(lambda x: x.translate(translator))
df.drug = df.drug.apply(lambda x: x.translate(translator))



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
df.drug = df.drug.apply(remove_stop)


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
    #fin_sen = ' '.join(ch for ch in fin_sen)
    return fin_sen

def pos_label(tokens):
    labels = nltk.pos_tag(tokens)
    return labels


#df.sentence = df.sentence.apply(lambda x: lemma(x))
#df.drug = df.drug.apply(lambda x: lemma(x))

print (df.sentence)

#drug_train = []
#i = 0
#while i < 5457:
#    drug_train.append(df.drug[i])
#    i += 1
#
#thefile = open('train_drug.txt', 'w')
#for item in drug_train:
#    thefile.write("%s\n" % item)
#
#drug_test = []
#i = 5457
#while i < 6139:
#    drug_test.append(df.drug[i])
#    i += 1
#
#outfile = open('test_drug.txt', 'w')
#for item in drug_test:
#    outfile.write("%s\n" % item)

#i = 0
#corpus = []
#while i < 6821:
#    corpus.append(df.sentence[i])
#    i += 1
    

#def save_doc(lines, filename):
#	file = open(filename, 'w')
#	file.write(lines)
#	file.close()
#    
#out_filename = 'sentences.txt'
#save_doc(corpus, out_filename)


















