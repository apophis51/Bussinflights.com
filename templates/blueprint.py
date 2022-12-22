from flask import Blueprint, render_template

example_blueprint = Blueprint('example_blueprint', __name__)
#second = Blueprint('example_blueprint', __name__, template_folder='templates')



@example_blueprint.route('/')
def index():
    return "This isdd an exdamddple app"
@example_blueprint.route('/h/')
def whatever():
    return render_template("cool.html")