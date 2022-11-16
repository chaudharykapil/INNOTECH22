from flask import Flask, render_template, flash, request,redirect,session

from models import Manager

import requests

from extensions import db

from datetime import datetime

app = Flask(__name__)
app.app_context().push()


app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://kapil829:ashish1234#@kapil829.mysql.pythonanywhere-services.com/kapil829$innotech'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:kapil@localhost/innotech'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def Home():
    data = Manager.query.all()
    db.session.close()
    print(data)
    return render_template("Maintable.html",data = data)


@app.route('/api/sendcoord')
def  coordinate():
    #res = requests.get(api_url)
    latlong = request.args.get('latlong')
    if(latlong and len(latlong) > 0):
        coord = latlong.split(" ")
        if(coord and len(coord)>=2):
            manger = Manager(
                Latitude = coord[0],
                Longitude = coord[1],
                time = str(datetime.now()),
                name = ""
                )
            db.session.add(manger)
            db.session.commit()
            db.session.close()
            return "1"
        return "0"
    return "0"

#app.run(debug=True)