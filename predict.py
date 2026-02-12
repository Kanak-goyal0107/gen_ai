import nltk
#nltk.download('punkt_tab')
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib

import string
punc = string.punctuation
def preprocess_text(sentences):
  clean=[]
  punctuate = string.punctuation
  engStopwords = stopwords.words("english")
  wNet = WordNetLemmatizer()
  for sentence in  sentences:
    sentence = sentence.lower()
    sentence = word_tokenize(sentence)
    sentence = [word for word in sentence if word not in punctuate]
    sentence = [word for word in sentence if word not in engStopwords]
    for word in sentence:
      word = wNet.lemmatize(word, "v")
      cleaned=" ".join(sentence)
    clean.append(cleaned)
  return clean
vectorizer = joblib.load("tfidf.pkl")
logistic = joblib.load("intent_clf_model.pkl")
user_input = "hola"
processed = preprocess_text([user_input])
user_vector = vectorizer.transform(processed)
prediction = logistic.predict(user_vector)
print(prediction)