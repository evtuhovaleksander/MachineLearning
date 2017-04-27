import nltk
import string
from nltk.corpus import stopwords



def tokenize_me(file_text):
    tokens = nltk.word_tokenize(file_text)  # токенезация

    tokens = [i for i in tokens if (i not in string.punctuation)]  # удаление пунктуации

    stop_words = stopwords.words('russian')
    stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на'])
    tokens = [i for i in tokens if (i not in stop_words)]

    # cleaning words
    tokens = [i.replace("«", "").replace("»", "") for i in tokens]

    return tokens


print(tokenize_me('шла саша по шоссе и сосала сушку'))
