from flask import Blueprint, render_template, request
#from flask_ckeditor import CKEditorField, CKEditor
import openai  #new
import os.path
import re

example_blueprint = Blueprint('example_blueprint', __name__)
#second = Blueprint('example_blueprint', __name__, template_folder='templates')
openai.api_key = "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" #new

myprompt = """make a 4 paragraph blog about Flights to 

start every new paragraph with '#'
separate the questions on its own line
make an introduction about

"""

@example_blueprint.route('/mypost/')
def mypost():
    if request.method == 'POST':
       # title = request.form['title']
      #  content = request.form['content']
        #name = request.form['name']
        return render_template("cool.html",myprompt=myprompt)
    return render_template("cool.html",myprompt=myprompt)
@example_blueprint.route('/mypostt/', methods=['GET', 'POST'])
def myypost():
    #first = request.args.get('content')
    first = request.form['content']  


##first we capitalize our h2 titles in capital case added 2/3/20223
    find = re.compile(r'<h2>(.*?)</h2>')
    results = find.findall(first)
    for x,y in enumerate(range(len(results))):
        first = first.replace(results[x], results[x].title())
    #### end 2/3/2023 edit






    ###print splitter added 1/19/2023
    return_string = ""
    second = first.rsplit("*")   #2/3/2023  this is just a note we should make second more descript and make it say blog_rough_draft
    

    for x in second:
        for y in x.rsplit("?"):
           # re.sub('<[^<]+?>', '', y)
            y = y.replace("<p>", "")
            y = y.replace("<br>", "")
            y = y.replace("</p>", "")
            return_string = return_string + y + "\r"
            print(y)
            print('\n')
            #print(y +"?")
    ###end print splitter 1/19/2023
    return render_template("cool.html", first=first,return_string=return_string)

@example_blueprint.route('/gpt3/', methods=['GET', 'POST'])
def gpt3():
    first = request.form['content']
    response = openai.Completion.create(
            model="text-davinci-003",
            max_tokens=2000,
            prompt=first,
            temperature=0.6)

    ##edit 1/19/2023
    ##end 1/19/2023 edit
    first=first + response.choices[0].text    
    return render_template("cool.html", first=first)






blog ="""
\n{% extends "base.html" %}
\n{% block h1 %}{% block title %}TTT{% endblock %}{% endblock %}
\n{% block travel %}  {% include "poland-flights/poland-base.html" %}{% endblock travel%}
\n{% block flag %}<img class="bodyphoto visainfodiv" src="/static/polandflag.png">{% endblock flag%}
\n{% block travelphoto %} <img class="bodyphoto" src="/static/nice view of poland.png">{% endblock %}


\n{% block widget %}
\n***
\n{% endblock widget%}


\n<div class = "white">
\n{% block visa %} <p class= "smallfont">Get Current Visa Information From <a href="https://www.visahq.com/poland/"
        rel="sponsored">VisaHQ</a></p>
\n {% endblock %}

\n{% block content %}
\n ###

\n<em>
\n    <strong>Before booking your trip, make sure to compare flights and prices to get the most out of your experience. To
        get started, check out FlightTicketFinder.com flight tracker for the best deals and discounts on <a
            href="/poland-flights/">flights to poland.</a></strong>
\n</em>
\n</div>
\n{% endblock %}
"""



@example_blueprint.route('/print/', methods=['GET', 'POST'])
def printt():
    content = request.form['content']
    
    title = request.form['title']
    widget_data = request.form['widget_data'] ## 1/18/2023 edit
    route = title.replace(" ","-")
    url = title.replace(" " , "-") + ".html"
    urlwithouthtml = title.replace(" ", "-")
    method = title.replace(' ', '')
    print(title)
    print(url)
    print(method)

    navigation = f"""
    \n\n<li>
     \n <a href = "/poland-flights/{urlwithouthtml}/">{title}</a>
   \n </li>
   \n
    """
    #writes everything here instead of individual files
    #text = open(f"{url}","a")
    #text.writelines(blog.replace("TTT",title).replace("###",content))
    #text = open('example_blueprint.py', 'a')
    #text.writelines(f'\n@poland_blueprint.route("/{route}/") #ai-generated')
    #text.writelines(f'\ndef {method}(): #ai-generated')
    #text.writelines(f'\n\treturn render_template("/poland-flights/{url}") #ai-generated')
    #text.writelines(navigation)
    #return render_template("cool.html", first=content)

    save_path = r"C:\Users\malco\Bussinflights.com\templates\poland-flights" 
    filelocation = f"{url}"
    completeName = os.path.join(save_path, filelocation)
    text = open(completeName,"a")
    #text.writelines(blog.replace("TTT",title).replace("###",content)) depricated and added ***
    content = content.replace("’","'")#added this line to correct messed up unicode characters incomming from gpt3
    text.writelines(blog.replace("TTT",title).replace("###",content).replace("***",widget_data))
    text = open('poland_blueprint.py', 'a')
    text.writelines(f'\n@poland_blueprint.route("/{route}/") #ai-generated')
    text.writelines(f'\ndef {method}(): #ai-generated')
    text.writelines(f'\n\treturn render_template("/poland-flights/{url}") #ai-generated')
    
    filelocation = "poland-base.html"
    completeName = os.path.join(save_path, filelocation)


    text = open(completeName,"r")
    data = text.readlines()
   # data = data[len(data)-2]+ navigation
    data[len(data)-4] = navigation
    text = open(completeName,"w")
    text.writelines(data)
    #text.writelines(navigation)
    #data[-1] = navigation
    

    #return render_template("cool.html", first=content)       depricated 1/19/2023

    return_navigation = f"/poland-flights/{urlwithouthtml}/"

    return render_template("cool.html", first=content,url = "http://127.0.0.1:5000" + return_navigation)
    