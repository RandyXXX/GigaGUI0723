from flask import Flask ,redirect,url_for

app=Flask(__name__)

@app.route("/tiger")
def hello_tiger():
    return '[T] is Tiger'

@app.route("/lion")
def hello_lion():
    return '[L] is Lion'

@app.route("/new/<animal>")
def hello_nothing(animal):
    return "[N] New Animal %s" % animal

@app.route("/animal/<kind>")
def hello_animal(kind):
    if kind=="tiger":
        return redirect(url_for("hello_tiger"))
    if kind=="lion":
        return redirect(url_for("hello_lion"))
    else:
        return redirect(url_for("hello_nothing",animal=kind))


if  __name__ =="__main__":
    app.run(debug=True)