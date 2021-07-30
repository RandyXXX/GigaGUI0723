from flask import Flask

app=Flask(__name__)

@app.route("/")
def HelloWorld():
    return "aaaaaaaFFFFFFFFFGGGGGGGGAAAAAA"


def create_app():
    return app