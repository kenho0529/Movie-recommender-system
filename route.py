from flask import Flask, render_template, url_for, redirect, request, jsonify
from movie_rs import movie_RS
from movie_poster import get_poster_url

#Home page of the app

app= Flask(__name__)

@app.route("/")
def home():

    return render_template("movie.html")


#Recommend page
@app.route('/recommend', methods=['POST'])
def recommend():
	movie_title=request.form.get('Movie_title')

	result=movie_RS(str(movie_title)).recommend()

	poster_url=[]
	try:
		for i in range(len(result)):
			poster_url.append(get_poster_url(result[i]))
	except:
		poster_url=[]


 	
	return render_template('recommend.html', movies=result, movie_url=poster_url)


if __name__ =='__main__':
	app.run(debug=True)

