import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle

#Import Data
df=pd.read_csv('data/combined_df.csv')
df['lemmatized']=df['lemmatized'].apply(lambda x:x.split(','))

#TF-IDF all information
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix_all = tf.fit_transform(df['all_feature'])
cosine_sim_all = linear_kernel(tfidf_matrix_all, tfidf_matrix_all)

#Save the cosine similarity matrix
pickle_out = open("cosine.pickle","wb")
pickle.dump(cosine_sim_all, pickle_out)
pickle_out.close()