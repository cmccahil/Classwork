import sys
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from sklearn import metrics
import time

columnsToRemove = ["id", "source", "user_id", "truncated", "in_reply_to_status_id",
                   "in_reply_to_user_id", "in_reply_to_screen_name", "retweeted_status_id", "geo", "place",
                   "contributors", "retweet_count", "reply_count", "favorite_count", "favorited", "retweeted",
                   "possibly_sensitive", "num_hashtags", "num_urls", "num_mentions", "created_at", "timestamp",
                   "crawled_at", "updated"]


def print_elapsed(msg, start_time):
    print("%s seconds" % (time.time() - start_time))
    print(msg, end="")
    return time.time()


def main():
    file = sys.argv[1]
    start_time = time.time()
    print("reading " + file + "...", end="")
    df = pd.read_csv(file, header=0)

    # remove columns other than label and text
    start_time = print_elapsed("deleting columns...", start_time)
    for column in columnsToRemove:
        del df[column]

    start_time = print_elapsed("replacing links...", start_time)
    df['text'] = df.text.str.replace('https*://[a-zA-Z0-9\./]+', ' link ')

    start_time = print_elapsed("converting to lowercase...", start_time)
    df['text'] = df['text'].str.lower()

    start_time = print_elapsed("removing punctuation...", start_time)
    df['text'] = df.text.str.replace('[^\w\s]', '')

    start_time = print_elapsed("tokenizing...", start_time)
    df['text'] = df['text'].fillna("").map(nltk.word_tokenize)

    start_time = print_elapsed("stemming...", start_time)
    stemmer = PorterStemmer()
    df['text'] = df['text'].apply(lambda x: [stemmer.stem(y) for y in x])

    start_time = print_elapsed("combining stems...", start_time)
    df['text'] = df['text'].apply(lambda x: ' '.join(x))

    start_time = print_elapsed("transforming...", start_time)
    count_vect = CountVectorizer()
    counts = count_vect.fit_transform(df['text'])
    transformer = TfidfTransformer().fit(counts)
    counts = transformer.transform(counts)

    start_time = print_elapsed("training the model...", start_time)
    X_train, X_test, y_train, y_test = train_test_split(counts, df['label'], test_size=0.1, random_state=42)

    model = MultinomialNB().fit(X_train, y_train)

    predicted = model.predict(X_test)
    matrix = metrics.confusion_matrix(y_test, predicted)
    print_elapsed(matrix, start_time)
    print("\nAccuracy:", np.mean(predicted == y_test))


if __name__ == "__main__":
    main()
