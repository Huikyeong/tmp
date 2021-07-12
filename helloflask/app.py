from flask import Flask, render_template, request

app = Flask(__name__)
# app.debug = True
'''
@app.before_request
def before_request():
    print("before_request!!")
    g.str = "한글"

@app.route("/gg")
def helloworld2():
    return "Hello World!" + getattr(g, 'str', '111')
'''

@app.route("/")
def first():
    if request.method == 'GET':
        pageX = request.args.get('pageX')
        pageY = request.args.get('pageY')
        print(pageX, pageY)
    return render_template("touch_event.html")

@app.route("/touch", methods = ['GET'])
def touch():
    pageX = request.args.get("pageX")
    pageY = request.args.get("pageY")
    print(pageX, pageY)
    return render_template("touch_event2.html")


if __name__ == "__main__":
    app.run(host = '0.0.0.0')