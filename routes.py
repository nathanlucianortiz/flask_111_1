"""Flask routes"""

# from the app module import the app variable
from app import app

# A line prefixed by "@"" is a decorator in python
# We are using the route function to map a view function to a route
@app.route("/")
def index():    # The view function
    return "Hello, World"


@app.route("/aboutme")
def aboutme():
    my_dictionary = dict()
    my_dictionary["first_name"] = "Nathan"
    my_dictionary["last_name"] = "Ortiz"
    my_dictionary["hobbies"] = "Space Exploration"

    return my_dictionary

@app.route("/aboutme2")
def aboutme_html():
    first_name = "Nathan"
    last_name = "Ortiz"
    hobbies = "Space Exploration"
    about_me = """<h1 style="color:red;">First name: %s; <br>
                  Last_name: %s; <br>
                  Hobbies: %s</h1>""" %(
                      first_name,
                      last_name,
                      hobbies)
    return about_me