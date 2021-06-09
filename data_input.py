import pickle
import numpy as np
import pandas as pd
from gensim.models import LdaModel

df=pd.read_csv('data/combined_df.csv')
df['lemmatized']=df['lemmatized'].apply(lambda x:x.split(','))

dict_dist = open("data/dict.pickle","rb")
doc_topic_dist = pickle.load(dict_dist)

cosine_pickle = open("data/cosine.pickle","rb")
cosine_sim_all=pickle.load(cosine_pickle)

lda = LdaModel.load('LDA/lda_combined_review')

corpus_pickle = open("LDA/corpus.pickle","rb")
corpus=pickle.load(corpus_pickle)

dictionary_pickle = open("LDA/dictionary.pickle","rb")
dictionary=pickle.load(dictionary_pickle)