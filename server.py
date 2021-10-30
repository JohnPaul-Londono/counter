from flask import Flask, render_template,redirect,session, request
app = Flask(__name__)
app.secret_key="keepitsecret"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter']+=1
    #session['counter']+={{int}}
    return render_template("index.html", add=session['counter'] ) #increment=session['counter']

@app.route('/add2', methods=['POST'])
def add2():
    session['counter'] = session['counter'] + 1
    return redirect("/")

# @app.route('/manually', methods=['POST'])
# def manual():
#     session['counter'] = session['counter'] + {{int}}
#     return redirect("/")

@app.route("/destroy_session", methods=['POST'])
def destroy_session():
    session.clear()
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True)