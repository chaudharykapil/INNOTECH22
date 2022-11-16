from flask import Flask, render_template, flash, request,redirect,session

from models import Manager

import requests

from extensions import db

from datetime import datetime

app = Flask(__name__)
app.app_context().push()


app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://kapil829:ashish1234#@kapil829.mysql.pythonanywhere-services.com/kapil829$innotech'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api_url = "http://api.positionstack.com/v1/reverse?access_key=65aa3458e8ba59795182408ec196f7af&query=28.693138,77.533440"
#api_url = "http://api.positionstack.com/v1/forward? access_key = 65aa3458e8ba59795182408ec196f7af& query = 1600 Pennsylvania Ave NW, Washington DC"
@app.route('/')
def  coordinate():
    #res = requests.get(api_url)
    latlong = request.args.get('latlong')
    if(latlong and len(latlong) > 0):
        coord = latlong.split(" ")
        manger = Manager(
            Latitude = coord[0],
            Longitude = coord[1],
            time = str(datetime.now()),
            name = ""
            )
        db.session.add(manger)
        db.session.commit()
        return "1"
    return "0"