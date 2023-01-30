from flask import Flask, Blueprint, render_template, request

australia_blueprint = Blueprint('australia_blueprint' , __name__)


### Mexico
@australia_blueprint.route("/") #ai-generated
def AustraliaFlights(): #ai-generated
	return render_template("/australia-flights/Australia-Flights.html") #ai-generated
@australia_blueprint.route("/Flights-from-LAX-to-Australia/") #ai-generated
def FlightsfromLAXtoAustralia(): #ai-generated
	return render_template("/australia-flights/Flights-from-LAX-to-Australia.html") #ai-generated
@australia_blueprint.route("/Flights-from-Hawaii-to-Australia/") #ai-generated
def FlightsfromHawaiitoAustralia(): #ai-generated
	return render_template("/australia-flights/Flights-from-Hawaii-to-Australia.html") #ai-generated
@australia_blueprint.route("/Flights-from-New-Zealand-to-Australia/") #ai-generated
def FlightsfromNewZealandtoAustralia(): #ai-generated
	return render_template("/australia-flights/Flights-from-New-Zealand-to-Australia.html") #ai-generated
@australia_blueprint.route("/New-York-to-Australia-Flight/") #ai-generated
def NewYorktoAustraliaFlight(): #ai-generated
	return render_template("/australia-flights/New-York-to-Australia-Flight.html") #ai-generated
@australia_blueprint.route("/Flights-from-Miami-to-Australia/") #ai-generated
def FlightsfromMiamitoAustralia(): #ai-generated
	return render_template("/australia-flights/Flights-from-Miami-to-Australia.html") #ai-generated
@australia_blueprint.route("/Flights-from-Guam-to-Australia/") #ai-generated
def FlightsfromGuamtoAustralia(): #ai-generated
	return render_template("/australia-flights/Flights-from-Guam-to-Australia.html") #ai-generated
@australia_blueprint.route("/Flights-from-Florence-to-Australia/") #ai-generated
def FlightsfromFlorencetoAustralia(): #ai-generated
	return render_template("/australia-flights/Flights-from-Florence-to-Australia.html") #ai-generated
@australia_blueprint.route("/Flights-from-Egypt-to-Australia/") #ai-generated
def FlightsfromEgypttoAustralia(): #ai-generated
	return render_template("/australia-flights/Flights-from-Egypt-to-Australia.html") #ai-generated
@australia_blueprint.route("/Flights-from-Denver-to-Sydney/") #ai-generated
def FlightsfromDenvertoSydney(): #ai-generated
	return render_template("/australia-flights/Flights-from-Denver-to-Sydney.html") #ai-generated
@australia_blueprint.route("/Flights-from-the-USA-to-Australia/") #ai-generated
def FlightsfromtheUSAtoAustralia(): #ai-generated
	return render_template("/australia-flights/Flights-from-the-USA-to-Australia.html") #ai-generated