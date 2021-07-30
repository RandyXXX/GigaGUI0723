from flask import Flask
print(__name__)
app=Flask(__name__)

@app.route('/')
def HelloWorld():
    return "AAAAAAAAAAAA"

app.run(port=2345,host="0.0.0.0",debug=True)