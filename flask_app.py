
from flask import Flask, render_template, request
from colombia_blueprint import colombia_blueprint


app = Flask(__name__)
app.register_blueprint(colombia_blueprint, url_prefix='/colombia-flights')

'''
@app.route('/')
def hello_world():
    return 'Hellof from Flask!'

@app.route("/home")
def home():
    some_variable = "malcolm"
    letters = list(some_variable)
    mylist=[1,2,3,4,5]
    userlogedin = True
    return render_template("tutorial.html",my_variable=some_variable, letters=letters,mylist=mylist,userlogedin=userlogedin)


@app.route('/fuck/')
def hello_worldd():
    return render_template("tutorial.html")
'''
@app.route('/')
def home():
    return render_template("home.html")
    
@app.errorhandler(404)
def page_not_found(e):
    return  render_template('404.html'), 404
#locatio pages
@app.route("/tulum-mexico/")
def tulumnmeta():
    return render_template("/locations/location-mexico-tulum-meta.html")
@app.route("/tulum-mexico/tulum-mexico-blog/")
def tulumn():
    return render_template("/locations/location-mexico-tulum.html")    

@app.route("/signup/")
def signup():
    return render_template("signup.html")

@app.route("/thankyou/")
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template("thankyou.html", first=first,last=last)

@app.route("/dontclick/")
def dontclick():
    return render_template("Dontclick.html")

