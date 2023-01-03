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


    ### cartagena

@colombia_blueprint.route("flights-to-cartagena-colombia/") #ai-generated
def FlightstoCartagenaColombia(): #ai-generated
	return render_template("/colombia-flights/Flights-to-Cartagena-Colombia.html") #ai-generated
@colombia_blueprint.route("/flights-to-cartagena-colombia-from-miami/") #ai-generated
def FlightstoCartagenaColombiaFromMiami(): #ai-generated
	return render_template("/colombia-flights/Flights-to-Cartagena-Colombia-From-Miami.html") #ai-generated
@colombia_blueprint.route("/flights-from-houston-to-cartagena-colombia/") #ai-generated
def flightsfromhoustontocartagenacolombia(): #ai-generated
	return render_template("/colombia-flights/flights-from-houston-to-cartagena-colombia.html") #ai-generated
@colombia_blueprint.route("cheap-flights-to-cartagena-colombia-from-nyc/") #ai-generated
def CheapFlightstoCartagenaColombiaFromNYC(): #ai-generated
	return render_template("/colombia-flights/Cheap-Flights-to-Cartagena-Colombia-From-NYC.html") #ai-generated

#####
@colombia_blueprint.route("/Flights-to-Cali-Colombia/") #ai-generated
def FlightstoCaliColombia(): #ai-generated
	return render_template("/colombia-flights/Flights-to-Cali-Colombia.html") #ai-generated



    
@colombia_blueprint.route("/Flights-Miami-to-Cali-Colombia/") #ai-generated
def FlightsMiamitoCaliColombia(): #ai-generated
	return render_template("/colombia-flights/Flights-Miami-to-Cali-Colombia.html") #ai-generated  
@colombia_blueprint.route("/Flights-From-NYC-to-Cali-Colombia/") #ai-generated
def FlightsFromNYCtoCaliColombia(): #ai-generated
	return render_template("/colombia-flights/Flights-From-NYC-to-Cali-Colombia.html") #ai-generated
@colombia_blueprint.route("/Flights-Orlando-to-Cali-Colombia/") #ai-generated
def FlightsOrlandotoCaliColombia(): #ai-generated
	return render_template("/colombia-flights/Flights-Orlando-to-Cali-Colombia.html") #ai-generated  
@colombia_blueprint.route("/Flights-From-Chicago-to-Cali-Colombia/") #ai-generated
def FlightsFromChicagotoCaliColombia(): #ai-generated
	return render_template("/colombia-flights/Flights-From-Chicago-to-Cali-Colombia.html") #ai-generated
@colombia_blueprint.route("/Non-Stop-Flights-to-Cali-Colombia/") #ai-generated
def NonStopFlightstoCaliColombia(): #ai-generated
	return render_template("/colombia-flights/Non-Stop-Flights-to-Cali-Colombia.html") #ai-generated
@colombia_blueprint.route("/Atlanta-to-Cali-Colombia-Flights/") #ai-generated
def AtlantatoCaliColombiaFlights(): #ai-generated
	return render_template("/colombia-flights/Atlanta-to-Cali-Colombia-Flights.html") #ai-generated
@colombia_blueprint.route("/Cheap-Flights-to-Cali-Colombia-From-London/") #ai-generated
def CheapFlightstoCaliColombiaFromLondon(): #ai-generated
	return render_template("/colombia-flights/Cheap-Flights-to-Cali-Colombia-From-London.html") #ai-generated
@colombia_blueprint.route("/Colombia-domestic-flights/") #ai-generated
def Colombiadomesticflights(): #ai-generated
	return render_template("/colombia-flights/Colombia-domestic-flights.html") #ai-generated
@colombia_blueprint.route("/Cheap-Flights-Panama-to-Colombia/") #ai-generated
def CheapFlightsPanamatoColombia(): #ai-generated
	return render_template("/colombia-flights/Cheap-Flights-Panama-to-Colombia.html") #ai-generated
@colombia_blueprint.route("/Colombia-Flights-From-LAX/") #ai-generated
def ColombiaFlightsFromLAX(): #ai-generated
	return render_template("/colombia-flights/Colombia-Flights-From-LAX.html") #ai-generatez
@colombia_blueprint.route("/Flights-to-Colombia-From-NYC/") #ai-generated
def FlightstoColombiaFromNYC(): #ai-generated
	return render_template("/colombia-flights/Flights-to-Colombia-From-NYC.html") #ai-generated
@colombia_blueprint.route("/Flights-From-Houston-to-Colombia/") #ai-generated
def FlightsFromHoustontoColombia(): #ai-generated
	return render_template("/colombia-flights/Flights-From-Houston-to-Colombia.html") #ai-generated
@colombia_blueprint.route("/Flights-from-Chicago-to-Colombia/") #ai-generated
def FlightsfromChicagotoColombia(): #ai-generated
	return render_template("/colombia-flights/Flights-from-Chicago-to-Colombia.html") #ai-generated
@colombia_blueprint.route("/Orlando-to-Colombia-Flights/") #ai-generated
def OrlandotoColombiaFlights(): #ai-generated
	return render_template("/colombia-flights/Orlando-to-Colombia-Flights.html") #ai-generated