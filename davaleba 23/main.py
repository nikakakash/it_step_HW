from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("main.html")





@app.route('/temp2')

def  temp2():
    return  render_template('temp2.html')


@app.route('/temp3')
def  temp3():
    return  render_template('temp3.html')


app.run(debug=True)