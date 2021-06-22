import imdb
   
# creating instance of IMDb
def get_movieid(movie):
    
    ia = imdb.IMDb()
    
    # name 
    
    # searching the name 
    search = ia.search_movie(movie)

    return 'tt'+str(search[0].movieID)

print(get_movieid('Source Code'))