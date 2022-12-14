from flask import Flask,render_template, request, redirect, session # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key=("thisismynonocounterkeydonttouch")


@app.route('/')
def index():

    if 'count'  in session:
        session['count']+=1
    return render_template("index.html", count= session['count'])

@app.route('/addtwo')
def addtwo():
    session['count']+=2
    return render_template("index.html", count= session['count'])

@app.route('/destory_session')
def reset():
    session['count'] = 0
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True, port=5001)    # Run the app in debug mode.
