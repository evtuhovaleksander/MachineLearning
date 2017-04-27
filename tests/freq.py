from pymorphy import get_morph
import sys
import codecs
import re
from nltk import *

def main():

    f = codecs.open(sys.argv[1], encoding='utf-8')
    raw = f.read()
    linex = raw.upper()
    # tokenize
    s = re.split(r'[\s+\t\n\.\|\:\/\,\!\"()]+', linex)
    # normalize
    vocabulary = []
    for i in s:
        if len(i) > 3:
            a = morph.get_graminfo(i,standard=True)
            if a:
                if a[0]['class'] not in ('-'): # classes (=> 'где-то, как-то') of stop-words
                    vocabulary.append(a[0]['norm'])
    fdist = FreqDist(vocabulary)
    for key in fdist.keys():
        print (key,':',fdist[key])

