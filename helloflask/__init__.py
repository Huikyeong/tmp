from flask import Flask, render_template

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
def helloworld():
    return render_template("touch_event.html")
