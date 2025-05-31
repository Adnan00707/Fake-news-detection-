import pandas as pd
import numpy as np 
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

# Load datasets
print("📂 Loading dataset...")
true = pd.read_csv('C:/Users/adnan/OneDrive/Desktop/fakenews/dataset/True.csv')
fake = pd.read_csv('C:/Users/adnan/OneDrive/Desktop/fakenews/dataset/Fake.csv')

# Combine and prepare
print("🧾 Preparing data...")
true['label'] = 1
fake['label'] = 0
news = pd.concat([fake, true], axis=0)
news = news.drop(['title', 'subject', 'date'], axis=1)
news = news.sample(frac=1).reset_index(drop=True)

# Clean text
print("🧼 Cleaning text...")
def wordopt(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\n', ' ', text)
    return text

news['text'] = news['text'].apply(wordopt)

# Split data
x = news['text']
y = news['label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# Vectorize
print("🔠 Vectorizing...")
vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)

# Train models
print("🤖 Training models...")
LR = LogisticRegression()
LR.fit(xv_train, y_train)

gbc = GradientBoostingClassifier()
gbc.fit(xv_train, y_train)

rfc = RandomForestClassifier()
rfc.fit(xv_train, y_train)

print("✅ Model is ready!")

from sklearn.metrics import classification_report

# Evaluate models
print("\n📊 Logistic Regression Report:")
print(classification_report(y_test, LR.predict(xv_test)))

print("\n🌲 Random Forest Classifier Report:")
print(classification_report(y_test, rfc.predict(xv_test)))

print("\n🚀 Gradient Boosting Classifier Report:")
print(classification_report(y_test, gbc.predict(xv_test)))


# Predict
def output_label(n):
    return "It is a Genuine News" if n == 1 else "It is a Fake News"

def manual_testing(news):
    test_df = pd.DataFrame({"text": [news]})
    test_df["text"] = test_df["text"].apply(wordopt)
    test_vector = vectorization.transform(test_df["text"])

    pred_lr = LR.predict(test_vector)
    pred_gbc = gbc.predict(test_vector)
    pred_rfc = rfc.predict(test_vector)

    return "\n\nLR Prediction: {}\nGBC Prediction: {}\nRFC Prediction: {}".format(
        output_label(pred_lr[0]),
        output_label(pred_gbc[0]),
        output_label(pred_rfc[0])
    )

news_article = input("📝 Enter a news article to test: ")
print(manual_testing(news_article))
