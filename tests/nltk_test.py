# Text Classification Demo Version
import nltk      #Connect to library
#nltk.usage(nltk.classify.ClassifierI)
from nltk.corpus import brown
import random
f=open("./check.txt")
text=f.read()
f.close()
words=nltk.tokenize.word_tokenize(text)            #Split text on words
stopw=open("./stop.txt")          #Text including stop words
stop=stopw.read()
stopw.close()
stopwords=nltk.tokenize.word_tokenize(stop)
filteredtext = [t for t in words        #Delete all stop words from input text
                if t.lower() not in stopwords]
filtertext = [word.lower() for word in filteredtext if word.isalnum()]
filttext=nltk.FreqDist(filtertext)
print(filttext)
print(filttext.keys())
test=[]
test.append(filttext.keys()[0])
test = filttext.keys()[:3]   #Find 3 most popular words
print(test)


def word_feats(words):
    return dict([(word,True) for word in words])

train_docs = [(word_feats(brown.words(fileid)),category)
             for category in brown.categories()
             for fileid in brown.fileids(category)]
test_docs = word_feats(test)
classifier = nltk.classify.NaiveBayesClassifier.train(train_docs)
print(classifier.classify(test_docs))