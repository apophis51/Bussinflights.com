
from flask import Flask, render_template, request
from colombia_blueprint import colombia_blueprint
from mexico_blueprint import mexico_blueprint
from australia_blueprint import australia_blueprint
from poland_blueprint import poland_blueprint

from example_blueprint import example_blueprint

app = Flask(__name__)
app.register_blueprint(colombia_blueprint, url_prefix='/colombia-flights')
app.register_blueprint(mexico_blueprint, url_prefix='/mexico-flights')
app.register_blueprint(australia_blueprint, url_prefix='/australia-flights')
app.register_blueprint(poland_blueprint, url_prefix='/poland-flights')
app.register_blueprint(example_blueprint, url_prefix='/example')


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


@app.route('/gfdg/')
def hello_worldd():
    return render_template("tutorial.html")

def b():
    def c():
        @app.route('/b')
        def t():
            return render_template("tutorial.html")
    return c()
'''
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/sitemap/')
def sitemap():
    return render_template("sitemap.txt")
    
@app.errorhandler(404)
def page_not_found(e):
    return  render_template('404.html'), 404
#locatio pages
 

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

