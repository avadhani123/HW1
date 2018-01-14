
## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".
#ankita avadhani
#Worked wih will chatterson
import json
import requests
from datetime import datetime as dt
import html

## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Welcome to SI 364'

## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }
@app.route('/movie/<name>')
def mov(name):
    url = "http://itunes.apple.com/search"
    params = {"media": "movie", "term": name}
    get_name = requests.get(url, params = params)
    json_format = json.loads(get_name.text)
    return get_name.text

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.
@app.route('/question')
def entry():
    m = """<DOCTYPE html>
<html>
<body>
<div>
<form action = "/result" method = "GET">
    Enter your Favorite Number:
    <input type= "text" name = "number" value = "0">
    <br> <br>
    <input type = "submit" value = "Submit"
<div>
</form>
</htm>
"""
    return m

@app.route('/result', methods= ['POST', 'GET'])
def double():
    if request.method == 'GET':
        number = request.args.get('number', '')
        num = int(number)
        return "Double your favorite number is: " + str(num*2)
## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

@app.route('/music',methods= ['POST','GET'])
def enter_song():
    s = """<!DOCTYPE html>
<html>
<body>
<form action="http://localhost:5000/result/artistname" method="GET">
  Who sang the song "Closer"?:<br>
  <input type="radio" name="artist" value="Demi Lovato" checked> Demi Lovato<br>
  <input type="radio" name="artist" value="Bruce Springsteen"> Bruce Springsteen<br>
  <input type="radio" name="artist" value="The Chainsmokers"> The Chainsmokers <br>
  <input type="submit">
</form> 
</body>
</html>""" 
    return s

@app.route('/result/artistname', methods = ['POST', 'GET'])
def music_view():
    if request.method == 'GET':
    	result = request.args
    	artistname = result.get('artist')
    	if artistname == "Demi Lovato":
    		response_display = "Try Again! Hint: They are EDM."
    	if artistname == "Bruce Spingsteen":
    		response_display = "Try Again! Hint: They are EDM."
    	if artistname == "The Chainsmokers":
    		response_display = "Correct"
    	return response_display



    	# artistname = artistname
    	# baseurl = "https://itunes.apple.com/search"

    	# # artist_name = result.get('artist')
    	# params = {"entity": "music", "term": artistname}
    	# resp = requests.get(baseurl,params=params)
    	# data_text = resp.text
    	# python_obj = json.loads(data_text)
    	# data_return = json.dumps(python_obj, indent = 2)
    	# print(data_return)
    	# return data_return


        # return render_template("result.html",result = result)
        ## GET request got sent to the result route/result place. if the request method was GET, this means the GET request sent some stuff here, can get argumetns from the GET request and pull them out by their names. can show them on a page and render them in the same way. 

