from time import time
import pandas as pd
from sklearn.linear_model import LogisticRegressionCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

print("Loading data")
tick = time()
df = pd.read_csv("NYC_311_20180101_through_20190930.csv")
print("{} elapsed".format(time() - tick))

# downsample data for speed and pull out a priori relevant features, create raw data
print("Data munging")
tick = time()
df_sample = df.sample(frac=0.1)
data = df_sample[['Complaint Type', 'Descriptor', 'Location Type']]
targets = df_sample['Agency']
data = data.rename(columns={"Complaint Type":"complaint_type", "Descriptor":"descriptor", "Location Type":"location_type"})
data = data.fillna(value="")

raw_text = []
for row in data.itertuples():
    # join data columns into raw text blob
    try:
        tmp_text = " ".join([row.complaint_type, row.descriptor, row.location_type])
    except Exception:
        print(row)
        break
    raw_text.append(tmp_text)
print("{} elapsed".format(time() - tick))

print("Split data & fit vectorizer/classifier")
tick = time()
# train/test split
X_train, X_test, y_train, y_test = train_test_split(raw_text, targets, test_size=0.1, random_state=19)
# BoNG (size=1,2)
vec = CountVectorizer(ngram_range=(1,2), lowercase=True, binary=False, stop_words="english")
# LogisticRegression with automatic regularization tuning
lr = LogisticRegressionCV(class_weight="balanced")
# fit on train data
lr.fit(vec.fit_transform(X_train), y_train)
print("{} elapsed".format(time() - tick))

print("\nEVAL on held-out data\n")
# eval on test
print(classification_report(y_test, lr.predict(vec.transform(X_test)), digits=3))
