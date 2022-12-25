from flask import Blueprint, render_template, request
from flask_ckeditor import CKEditorField, CKEditor

example_blueprint = Blueprint('example_blueprint', __name__)
#second = Blueprint('example_blueprint', __name__, template_folder='templates')



@example_blueprint.route('/')
def index():
    return "Tdfdfsfhis isdffffd an exdamddple app"
@example_blueprint.route('/h/')
def whatever():
    return render_template("cool.html")
@example_blueprint.route('/mypost/')
def mypost():
    if request.method == 'POST':
       # title = request.form['title']
      #  content = request.form['content']
        #name = request.form['name']
        return render_template("cool.html")
    return render_template("cool.html")
@example_blueprint.route('/mypostt/', methods=['GET', 'POST'])
def myypost():
    first = request.args.get('content')
    first = request.form['content']
    print(type(first))
    return render_template("cool.html", first=first)
