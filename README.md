# Movie-recommender-system


## Description
This is to build a hybrid movie recommendation system, which has combined the contents from movies' description and reviews. TF-IDF is used for data transformations and LDA is implmented to extract latent topic from reviews. The cosine similarity and Jensen–Shannon distance are used to calculate the similarity of the documents.

![Flowchart](/images/flowchart.png)

## Data
I have used the data of rotton tomatoes from Kaggle.  
Original Data:  
[Kaggle](https://www.kaggle.com/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset)

The reviews and movie database are preprossed. The reviews DB is tokenized and lemmatized. Since it takes extremely long for lemmatization, the process is done before. A lemmatized database can be found below.

## How to run
1. Download the whole file and unzipped the data in data file.
2. Run cosine_matrix.py to get the cosine similarity matrix for saving time.
3. Place the cosine pickle to data file.
4. Run movie_model.py.

## Packages required
- Numpy
- Pandas
- Gensim
- Scipy
- Pickle
