import numpy as np
import pandas as pd
from gensim import corpora
from scipy.spatial import distance
from data_input import df,doc_topic_dist, cosine_sim_all, lda, corpus,dictionary

class movie_RS():
    
    def __init__(self, movie_title):
        self.movie_title=movie_title
        self.lda=lda
        self.corpus=corpus
        self.dictionary=dictionary
        self.cosine_sim=cosine_sim_all
        self.doc_topic_dist=doc_topic_dist
    

    #Calculate the weighted rating based on IMDB formula
    def weighted_rating(self, x, m, C):
        v = x['audience_count']
        R = x['audience_rating']
        return (v/(v+m) * R) + (m/(m+v) * C)

    def jensen_shannon(self,query, matrix):
    
        sim = [distance.jensenshannon(data,query) for data in matrix]
        return sim


    def combine_score_rating(self, target_idx, movie_indices, sim_scores):
    
        movie_content_rating=df.iloc[target_idx]['content_rating']  
        movie_year=df.iloc[target_idx]['year']
        
        selected_movies=df.iloc[movie_indices]
        audience_counts = selected_movies[selected_movies['audience_count'].notnull()]['audience_count'].astype('int')
        
        m = audience_counts.quantile(0.5)

        C=selected_movies['audience_rating'].mean()
        wr=selected_movies.apply(lambda x: self.weighted_rating(x,m,C), axis=1)

        selected_df=pd.DataFrame(df[['movie_title','content_rating','year','audience_rating','audience_count']].iloc[movie_indices])
        selected_df['Score']=[x[1] for x in sim_scores]
        selected_df['wr']=wr
        #Product for similarity and rating so priortise to recommend high similarity and high rating movies
        
        selected_df['mix_score']=selected_df['wr']*selected_df['Score']
        
        
        #Set the limit for number of audience count
        #At least higher than 50% quantile of the audience count in the whole document
        count_bound=df['audience_count'].quantile(0.5)
        #Remove movie that is over the target movie content rating and with too few audience
        #ranked by the mix score
        #Only select movie that is too old compared with the target movie, threshold is a decade-10 years.
        selected_df=selected_df[(selected_df['content_rating']<=movie_content_rating) & (selected_df['audience_count']>count_bound) & (selected_df['year']>movie_year-10)]
        selected_df=selected_df.sort_values('mix_score', ascending=False)

        # Return the top 10 most similar movies
        return selected_df[['movie_title','year','Score','audience_rating', 'audience_count']]

    def recommend(self,weight=0.5, n=6):
        indices = pd.Series(df.index, index=df['movie_title']).drop_duplicates()
        movie_list = df[df['movie_title'].str.contains(self.movie_title)]
        if len(movie_list):
            #In case of similar movie title like 'Iron Man' and 'Iron Man 2'
            if any(movie_list['movie_title']==self.movie_title):
                movie_title=self.movie_title
            else:
               # Pick the one with the highest audience rating
                movie_title=movie_list.sort_values(by=['audience_rating'], ascending=False)['movie_title'].iloc[0]
            
            print('Selected movie:',movie_title)
        
           #Some movies are duplicated such as Frozen has two version.
            #Pick the one with higher audience rating
            idx = indices[movie_title]
            if np.isscalar(idx)==False:
                idx=df.iloc[idx].sort_values(by=['audience_rating'], ascending=False).index[0]

              
            
            test_bow = self.dictionary.doc2bow(df.loc[idx]['lemmatized'])

            test_doc_distribution = np.array([tup[1] for tup in self.lda.get_document_topics(bow=test_bow)])
            lda_score=self.jensen_shannon(test_doc_distribution,self.doc_topic_dist)
            lda_score_inv=[1-x for x in lda_score]

            weight_score=zip([weight*x for x in lda_score_inv],[(1-weight)*y for y in self.cosine_sim[idx]])
            weighted_score=[x+y for x,y in weight_score]
            weight_rank=sorted(list(enumerate(weighted_score)), key=lambda x:x[1], reverse=True)[1:]

            weight_movie_indices = [i[0] for i in weight_rank]
            
            #Created another function for simplification 
            #Adding constraints to the  movie recommendation list
            recommend=self.combine_score_rating(idx,weight_movie_indices, weight_rank)
    
            #recommend=df_new.iloc[weight_movie_indices]
            #return df_new.iloc[weight_movie_indices[0:10]][['movie_title','actors','audience_rating']]
            print('=====================')
            result=[]
            for i in range(n):
                recommend_movie=recommend.iloc[i]['movie_title']
                movie_year=recommend.iloc[i]['year']
                #print(f"{i+1}. {recommend_movie}, {movie_year}")
                result.append(recommend_movie)
            return result
            #return recommend['movie_title'].head(n)
            
        else:
            x='Unknown'
            return x
            #print('No records in our database. Please check your input')


#x=input('Please select your movie:')
#def movie(movie):
#    print(movie_RS(movie).recommend())

#movie(x)

