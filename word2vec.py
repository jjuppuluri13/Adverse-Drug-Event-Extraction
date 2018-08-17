#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:53:53 2018

@author: jjuppuluri13
"""


import gensim
from gensim.models import Word2Vec
#import data_proc

print (df.sentence[9])

from nltk.tokenize  import word_tokenize
df.sentence = df.sentence.apply(lambda x: word_tokenize(x))

sentences = df.sentence
model = Word2Vec(sentences, size = 200, min_count = 1)
print(model)
words = list(model.wv.vocab)
#print(words)
#print(model['venlafaxine'])


#####               Export X train/test data
sequence = []
i = 0
while i < 5457:
    sequence.append(model[df.sentence[i]])
    i += 1


thefile = open('train_word.txt', 'w')
for item in sequence:
    thefile.write("%s\n" % item)
    
corp_test = []
i = 5457
while i < 6139:
    corp_test.append(model[df.sentence[i]])
    i += 1

expfile = open('test_word.txt', 'w')
for item in corp_test:
    expfile.write("%s\n" % item)

#####               Export y train/test data
drug_train = []
i = 0
while i < 5457:
    drug_train.append(model[df.drug[i]])
    i += 1

thefile = open('train_drug.txt', 'w')
for item in drug_train:
    thefile.write("%s\n" % item)

drug_test = []
i = 5457
while i < 6139:
    drug_test.append(model[df.drug[i]])
    i += 1

outfile = open('test_drug.txt', 'w')
for item in drug_test:
    outfile.write("%s\n" % item)
    
print (df.sentence[9])


#def save_doc(lines, filename):
#	file = open(filename, 'w')
#	file.write(lines)
#	file.close()
#    
#out_filename = 'sentences.txt'
#save_doc(corpus, out_filename)




# Word2Vec Visualization
#import sklearn
#from sklearn.decomposition import PCA
#import matplotlib
#from matplotlib import pyplot
#X = model[model.wv.vocab]
#pca = PCA(n_components=2)
#result = pca.fit_transform(X)
#pyplot.scatter(result[:, 0], result[:, 1])
#for i, word in enumerate(words):
#    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
##pyplot.axis([2.4,2.6,-0.02,0.02])
#pyplot.show()