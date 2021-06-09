from movie_rs import movie_RS
x=input('Please select your movie:')
def movie(movie):
	print(movie_RS(movie).recommend())

movie(x)
