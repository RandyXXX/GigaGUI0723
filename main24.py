from flask import Flask

app = Flask(__name__)

@app.route("/<int:count>/hi/<name>")
def greeting(count, name):
    str1 = 'hello'
    for _ in range(0, count):
        str1 += ' %s' % name
    return str1

# %f
# %.2f
# %.1f
# %10f
@app.route("/training1/<float:weight>/<path:goal>")
def another(goal,weight):
    str1 = 'my weight=%.3f, goal=%s' % (weight, goal)
    return str1

if __name__ == '__main__':
    app.run(port=5432, host='0.0.0.0', debug=True)