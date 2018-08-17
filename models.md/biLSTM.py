# LSTM for sequence classification in the IMDB dataset
import numpy
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
# fix random seed for reproducibility

def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

numpy.random.seed(7)
# load the dataset but only keep the top n words, zero the rest
top_words = 10000
#(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)
X_train = load_doc('train_word.txt')
y_train = load_doc('train_drug.txt')
X_test = load_doc('test_word.txt')
y_test = load_doc('test_drug.txt')
# truncate and pad input sequences
max_length = 25
X_train = sequence.pad_sequences(X_train, maxlen=max_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_length)
# create the model
embedding_vecor_length = 50
model = Sequential()
#model.add(Embedding(top_words, embedding_vecor_length, input_length=max_review_length))
model.add(LSTM(150))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, epochs=1, batch_size=16)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
