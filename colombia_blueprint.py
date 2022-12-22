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
    return render_template("/flights-to-colombia-from-london.html")