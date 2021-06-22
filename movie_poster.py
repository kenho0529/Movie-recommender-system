import requests
from imdb_id import get_movieid



def get_poster_url(movie_title):
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    KEY = '7538469672aec970a0eef0b3fcb444cc'

    url = CONFIG_PATTERN.format(key=KEY)
    r = requests.get(url)
    config = r.json()


    base_url = config['images']['base_url']
    sizes = config['images']['poster_sizes']
    """
        'sizes' should be sorted in ascending order, so
            max_size = sizes[-1]
        should get the largest size as well.        
    """
    def size_str_to_int(x):
        return float("inf") if x == 'original' else int(x[1:])
    max_size = max(sizes, key=size_str_to_int)
    movie_id=get_movieid(movie_title)

    IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}' 
    r = requests.get(IMG_PATTERN.format(key=KEY,imdbid=movie_id))
    api_response = r.json()
    try:
        posters = api_response['posters'][0]

        rel_path = posters['file_path']
        url = "{0}{1}{2}".format(base_url, max_size, rel_path)

        return url
    except:
        return False
