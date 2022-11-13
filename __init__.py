from flask import Flask, render_template, flash, request,redirect,session

from models import Manager
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")



from extensions import db

from datetime import datetime
    
app = Flask(__name__)
app.app_context().push()


app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ashish.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/coordinate')
def  coordinate():
    if(request.data):
        location_data=request.get_json()
        latitude=location_data["latitude"]
        longitude=location_data["longitude"]
        location = str(geolocator.geocode(latitude+","+longitude, language="en"))
        location=location[:90]
        time = str(datetime.now())
        print(type(time))
        manageinstance = Manager(
            Latitude=latitude, Longitude=longitude,name=location,time =time)
        

        db.session.add(manageinstance)
        db.session.commit()
        return "true"

if __name__ == "__main__":

    app.run(debug=True)
