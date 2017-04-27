from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# each phrase here could be document in your list
# of documents
my_phrases = ["богатый крутой много денег ",
              "бедный сыкло богатый мало денег "]

#  and you want to find the most similar document
#  to this document
phrase = ["богатый сыкло"]

# You could do it like this:
vectorizer = TfidfVectorizer(min_df=1, stop_words='english')
all_phrases = phrase + my_phrases
my_features = vectorizer.fit_transform(all_phrases)
scores = (my_features[0, :] * my_features[1:, :].T).A[0]
print(scores)
best_score = np.argmax(scores)
answer = my_phrases[best_score]
print(answer)