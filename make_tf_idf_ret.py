# Make files needed for TF-IDF

import json
from tqdm import tqdm
import flask
from flask import request, jsonify
from flask import Flask, render_template
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import argparse
import time
import joblib

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    tokens = word_tokenize(text.lower())
    tokens = [stemmer.stem(token) for token in tokens if token not in stop_words and token not in string.punctuation]

    return " ".join(tokens)

def main():
    video_wise_data = json.load(open("../path_to_ocr_file.json")) #ocr_file = [{"video_id": "" , "text": ""}, {"video_id": "", "text": ""}]

    corpus = []
    corpus_ids = []

    for i in tqdm(video_wise_data):
        corpus.append(i["text"])
        corpus_ids.append(i["video_id"])

    preprocessed_corpus = [preprocess_text(doc) for doc in corpus]

    start_time = time.time()

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_corpus)

    end_time = time.time()

    print("Total time taken: ")
    print(end_time-start_time)


    joblib.dump(tfidf_matrix, 'data_tfidf_matrix.pkl')
    joblib.dump(corpus_ids, 'data_corpus_ids.pkl')
    joblib.dump(vectorizer, 'data_vectorizer.pkl')

    print("files saved!")

if __name__=="__main__":
    main()