#flask is a library from which I am importing the class Flask
from flask import Flask
app = Flask(__name__)

@app.route("/wish")#creating an endpoint/path so that whenever /info is hit in the browser, this function is automatically created
def wish():
    return "<h1>Good Evening Docker!</h1>"

@app.route("/login")
def login():
    return "<h1>Here is the login page</h1>"

if __name__ == "__main__":
    app.run(port = 5000, host = "0.0.0.0")  #default port no for flask application=5000
                                            #from any computer we can access this flask application(0.0.0.0)
