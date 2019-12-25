from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_


@app.route("/")
def index():
    return render_template("feedback.html")
    
@app.route("/feedback2", methods=['POST'])
def success():
    if request.method=='POST':
         #email=request.form["bett"]
         height=request.form["optradio"]
         print(height) # height)
		 #data=Data(email,height)
         #db.session.add(data)
         #db.session.commit()
         return render_template("feedback2.html")
    #return redirect(url_for("index"))


@app.route("/feedback3", methods=['POST', 'GET'])
def success1():
    if request.method=='POST':
	    height=request.form["optradio"]
	    print(height) 
	    return render_template("feedback3.html")
    
    	 

@app.route("/feedback4", methods=['POST', 'GET'])
def success2():
    if request.method=='POST':
        height=request.form["optradio"]
        print(height) 
        return render_template("feedback4.html")
		
@app.route("/success", methods=['POST'])
def success3():		
    if request.method=='POST':
	    return render_template("success.html")
   	
   

if __name__ == '__main__':
    app.debug=True
    app.run()