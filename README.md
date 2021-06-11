# Movie-recommender-system


## Description
This is to build a hybrid movie recommendation system, which has combined the contents from movies' description and reviews. TF-IDF is used for data transformations and LDA is implmented to extract latent topic from reviews. The cosine similarity and Jensen–Shannon distance are used to calculate the similarity of the documents.

![Flowchart](/images/flowchart.png)

## Data
I have used the data of rotton tomatoes from Kaggle.  
Original Data:  
[Kaggle](https://www.kaggle.com/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset)

The reviews and movie database are preprossed. The reviews DB is tokenized and lemmatized. Since it takes extremely long for lemmatization, the process is done before. A lemmatized database can be found below.
Preprocessed Data and pickled model result (Please download whole file before running the model):  
Drive

## How to run
1. Download the whole file and preprocessed data
2. Run movie_model.py.

## Packages required
- Numpy
- Pandas
- Gensim
- Scipy
- Pickle
