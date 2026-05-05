import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("abc.cv")
X = df["reviews"]
y = df["sentiments"]
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size = 0.2, random_state = 47
)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec =  vectorizer.transform(X_test)
model = LogisticRegression()
model.fit(X_train_vec,y_train)
y_pred = model.predict(X_test_vec)
acc = accuracy_score(y_test,y_pred)
print(acc)
new_reviews = [
    "This movie was amazing",
    "The film was boring"
]
true_labels = ["positive", "negative"]
new_reviews_vec = vectorizer.transform(new_reviews)
new_reviews_pred = model.predict(new_reviews_vec)
print(accuracy_score(true_labels,new_reviews_pred))
