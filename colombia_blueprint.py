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
#flights to medellin colombia

@colombia_blueprint.route("/flights-to-colombia-medellin/")
def flightstocolombiamedellin():
    return render_template("/colombia-flights/flights-to-colombia-medellin.html")

@colombia_blueprint.route("/flights-to-medellin-colombia-from-miami/")
def flightstomedellincolombiafrommiami():
    return render_template("/colombia-flights/flights-to-medellin-colombia-from-miami.html")
@colombia_blueprint.route("/flights-from-orlando-to-medellin-colombia/")
def flightsfromorlandotomedellincolombia():
    return render_template("/colombia-flights/flights-from-orlando-to-medellin-colombia.html")
@colombia_blueprint.route("/cheap-flights-to-medellin-colombia-from-new-york/")
def cheapflightstomedellincolombiafromnewyork():
    return render_template("/colombia-flights/cheap-flights-to-medellin-colombia-from-new-york.html")
@colombia_blueprint.route("/flights-to-medellin-colombia-from-los-angeles/")
def flightstomedellincolombiafromlosangeles():
    return render_template("/colombia-flights/flights-to-medellin-colombia-from-los-angeles.html")


@colombia_blueprint.route("/flights-to-bogota-colombia/")
def flightstobogotacolombia():
    return render_template("/colombia-flights/flights-to-bogota-colombia.html")
@colombia_blueprint.route("/flights-miami-to-bogota-colombia/")
def flightsmiamitobogotacolombia():
    return render_template("/colombia-flights/flights-miami-to-bogota-colombia.html")
@colombia_blueprint.route("/flights-from-orlando-to-bogota-colombia/")
def flightsfromorlandotobogotacolombia():
    return render_template("/colombia-flights/flights-from-orlando-to-bogota-colombia.html")
@colombia_blueprint.route("/flights-from-lax-to-bogota-colombia/")
def flightsfromlaxtobogotacolombia():
    return render_template("/colombia-flights/flights-from-lax-to-bogota-colombia.html")
@colombia_blueprint.route("/flights-from-atlanta-to-bogota-colombia/")
def flightsfromatlantatobogotacolombia():
    return render_template("/colombia-flights/flights-from-atlanta-to-bogota-colombia.html")
@colombia_blueprint.route("/flights-fort-lauderdale-to-bogota-colombia/")
def flightsfortlauderdaletobogotacolombia():
    return render_template("/colombia-flights/flights-fort-lauderdale-to-bogota-colombia.html")

@colombia_blueprint.route("/flights-from-salt-lake-city-to-bogota-colombia/")
def flightsfromsaltlakecitytobogotacolombia():
    return render_template("/colombia-flights/flights-from-salt-lake-city-to-bogota-colombia.html")

