from flask import Flask, Blueprint, render_template, request

colombia_blueprint = Blueprint('colombia_blueprint' , __name__)


### Colombia
@colombia_blueprint.route("/")
def colombiaflights():
    return render_template("/colombia-flights/colombiaflights.html")
@colombia_blueprint.route("/Exploring-Colombia-All-You-Need-to-Know-Before-You-Go/")
def ExploringColombiaAllYouNeedtoKnowBeforeYouGo():
    return render_template("/colombia-flights/Exploring-Colombia-All-You-Need-to-Know-Before-You-Go.html")    
@colombia_blueprint.route("/cheap-flights-to-colombia/")
def cheapflightstocolombia():
    return render_template("/colombia-flights/cheap-flights-to-colombia.html")
@colombia_blueprint.route("/american-airlines-flights-to-colombia/")
def americanairlinesflightstocolombia():
    return render_template("/colombia-flights/american-airlines-flights-to-colombia.html")
@colombia_blueprint.route("/flights-to-colombia-from-london/")
def flightstocolombiafromlondon():
    return render_template("/colombia-flights/flights-to-colombia-from-london.html")

@colombia_blueprint.route("/flights-to-colombia-medellin/")
def flightstocolombiamedellin():
    return render_template("/colombia-flights/flights-to-colombia-medellin.html")

@colombia_blueprint.route("/cheap-flights-to-medellin-colombia/")
def cheapflightstomedellincolombia():
    return render_template("/colombia-flights/cheap-flights-to-medellin-colombia.html")
@colombia_blueprint.route("/flights-to-medellin-colombia-from-miami/")
def flightstomedellincolombiafrommiami():
    return render_template("/colombia-flights/flights-to-medellin-colombia-from-miami.html")
@colombia_blueprint.route("/flights-from-orlando-to-medellin-colombia/")
def flightsfromorlandotomedellincolombia():
    return render_template("/colombia-flights/flights-from-orlando-to-medellin-colombia.html")
@colombia_blueprint.route("/cheap-flights-from-miami-to-medellin-colombia/")
def cheapflightsfrommiamitomedellincolombia():
    return render_template("/colombia-flights/cheap-flights-from-miami-to-medellin-colombia.html")
@colombia_blueprint.route("/cheap-flights-to-medellin-colombia-from-new-york/")
def cheapflightstomedellincolombiafromnewyork():
    return render_template("/colombia-flights/cheap-flights-to-medellin-colombia-from-new-york.html")
@colombia_blueprint.route("/flights-to-medellin-colombia-from-los-angeles")
def flightstomedellincolombiafromlosangeles():
    return render_template("/colombia-flights/flights-to-medellin-colombia-from-los-angeles.html")