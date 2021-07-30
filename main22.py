from flask import Flask
from waitress import serve
import logging
print(__name__)
app=Flask(__name__)

@app.route('/')
def HelloWorld():
    return "AAAAAAAAAAAA1111"


if __name__=='__main__':
    #app.run(port=2345, host="0.0.0.0", debug=True)
    logger=logging.getLogger('waitress')
    logger.setLevel(logging.DEBUG)
    serve(app,host="0.0.0.0",port=2345)