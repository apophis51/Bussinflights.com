from flask import Flask, Blueprint, render_template, request

mexico_blueprint = Blueprint('mexico_blueprint' , __name__)


### Mexico
@mexico_blueprint.route("/") #ai-generated
def MexicoFlights(): #ai-generated
	return render_template("/mexico-flights/Mexico-Flights.html") #ai-generated
@mexico_blueprint.route("/tulum-mexico/")
def tulumnmeta():
    return render_template("/mexico-flights/location-mexico-tulum-meta.html")  


@mexico_blueprint.route("/Flights-from-LAX-to-Mexico-City/") #ai-generated
def FlightsfromLAXtoMexicoCity(): #ai-generated
	return render_template("/mexico-flights/Flights-from-LAX-to-Mexico-City.html") #ai-generated
@mexico_blueprint.route("/Flights-from-Tijuana-to-Mexico-City/") #ai-generated
def FlightsfromTijuanatoMexicoCity(): #ai-generated
	return render_template("/mexico-flights/Flights-from-Tijuana-to-Mexico-City.html") #ai-generated
@mexico_blueprint.route("/Houston-to-Mexico-City-Flights/") #ai-generated
def HoustontoMexicoCityFlights(): #ai-generated
	return render_template("/mexico-flights/Houston-to-Mexico-City-Flights.html") #ai-generated
@mexico_blueprint.route("/Flights-from-Denver-to-Mexico-City/") #ai-generated
def FlightsfromDenvertoMexicoCity(): #ai-generated
	return render_template("/mexico-flights/Flights-from-Denver-to-Mexico-City.html") #ai-generated
@mexico_blueprint.route("/Flights-From-Austin-to-Mexico-City/") #ai-generated
def FlightsFromAustintoMexicoCity(): #ai-generated
	return render_template("/mexico-flights/Flights-From-Austin-to-Mexico-City.html") #ai-generated
@mexico_blueprint.route("/Flights-to-Mexico-City-From-Phoenix/") #ai-generated
def FlightstoMexicoCityFromPhoenix(): #ai-generated
	return render_template("/mexico-flights/Flights-to-Mexico-City-From-Phoenix.html") #ai-generated
@mexico_blueprint.route("/Flights-From-NYC-to-Mexico-City/") #ai-generated
def FlightsFromNYCtoMexicoCity(): #ai-generated
	return render_template("/mexico-flights/Flights-From-NYC-to-Mexico-City.html") #ai-generated
    