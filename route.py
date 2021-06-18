from flask import Flask, render_template, url_for, redirect, request, jsonify
from movie_rs import movie_RS


#Home page of the app

app= Flask(__name__)

@app.route("/")
def home():

    return render_template("movie.html")

@app.route('/recommend', methods=['POST'])
def recommend():
 	movie_title=request.form.get('Movie_title')



 	result=movie_RS(str(movie_title)).recommend()


 	
 	return render_template('recommend.html', movies=result)


@app.route('/recommend_api', methods=['POST'])
def recommend_api():
	data= request.get_json(force=True)

	result=movie_RS(str(data)).recommend()



	return jsonify(result)
	
if __name__ =='__main__':
	app.run(debug=True)

