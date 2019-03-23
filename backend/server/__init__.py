import db, time, datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from pony.orm import *
from server.json import CustomJSONEncoder



app = Flask(__name__)
CORS(app)
app.json_encoder = CustomJSONEncoder


################################################################################
## Car park routes


@app.route("/carParks", methods=["GET"])
def get_car_parks():
    data = []
    with db_session:
        data = [d for d in db.CarPark.select()]
    return jsonify({
        "data": data if data else []
    })


@db_session
@app.route("/carParks", methods=["POST"])
def create_car_park():
    data = request.get_json()
    with db_session:
        db.db.insert("carpark", name=data["name"], capacity=data["capacity"])
    return "Success"


@db_session
@app.route("/carParks/<int:car_park_id>", methods=["GET"])
def get_car_park(car_park_id):
    data = []
    with db_session:
        data = [d for d in db.CarPark.select() if d.id == car_park_id]
    return jsonify({
        "data": data if data else []
    })


@db_session
@app.route("/carParks/<int:car_park_id>", methods=["PATCH"])
def update_car_park(car_park_id):
    data = request.get_json()
    # with db_session:
        # if "capacity" in data:
        #     db.CarPark.set(capacity=data["capacity"])
        # print("capacity" in data)
        # print("name" in data)
    return "In Progress"



@db_session
@app.route("/car-parks/<int:car_park_id>", methods=["DELETE"])
def delete_car_park(car_park_id):
    with db_session:
        db.CarPark[car_park_id].delete()
    return "Success"

################################################################################
## Price


@db_session
@app.route("/prices", methods=["GET"])
def get_prices():
    data = []
    with db_session:
        data = [d for d in db.Price.select()]
    return jsonify({
        "price": data if data else []
    })


@db_session
@app.route("/prices", methods=["POST"])
def create_price():
    data = request.get_json()
    with db_session:
        db.db.insert("price", price=data['price'], returning='id')
    return "{}"


@db_session
@app.route("/prices/<int:price_id>", methods=["GET"])
def get_price(price_id):
    data = {}
    with db_session:
        for d in db.Price.select():
            if d.id == price_id:
                data = d
                break
        if data == {}:
            print('I am here')
            db.db.insert("price", price=5, returning='id')
            for d in db.Price.select():
                if d.id == price_id:
                    data = d
                    break
    return jsonify({
        "price": data if data else {}
    })

@db_session
@app.route("/prices/<int:price_id>", methods=["PUT"])
def update_price(price_id):
    data = request.get_json()
    data = data['price']
    with db_session:
        db.Price[price_id].set(price=data['price'])
    return "{}"

@db_session
@app.route("/prices/<int:price_id>", methods=["DELETE"])
def delete_price(price_id):
    with db_session:
        db.Price[price_id].delete()
    return "{}"

################################################################################
## Happy hour routes


@db_session
@app.route("/happyHours", methods=["GET"])
def get_happy_hours():
    data = []
    with db_session:
        data = [d for d in db.HappyHour.select()]
    return jsonify({
        "happy-hour": data if data else []
    })


@db_session
@app.route("/happyHours", methods=["POST"])
def create_happy_hour():
    data = request.get_json()
    with db_session:
        db.db.insert("happyhour", happyhour=data['happyhour'], returning='id')
    return "Success"


@db_session
@app.route("/happyHours/<int:happy_hour_id>", methods=["GET"])
def get_happy_hour(happy_hour_id):
    data = {}
    with db_session:
        for d in db.HappyHour.select():
            if d.id == happy_hour_id:
                data = d
                break
        if data == {}:
            db.db.insert("happyhour", happyhour="6:00")
            for d in db.Price.select():
                if d.id == happy_hour_id:
                    data = d
                    break
    return jsonify({
        "happy-hour": data if data else {}
    })

@db_session
@app.route("/happyHours/<int:happy_hour_id>", methods=["PUT"])
def update_happy_hour(happy_hour_id):
    data = request.get_json()
    print(data)
    data = data['happyHour']
    with db_session:
        db.HappyHour[happy_hour_id].set(happyhour=data['happyhour'])
    return "{}"

@db_session
@app.route("/happyHours/<int:happy_hour_id>", methods=["DELETE"])
def delete_happy_hour(happy_hour_id):
    with db_session:
        db.HappyHour[happy_hour_id].delete()
    return "{}"


################################################################################
## Ticket routes

@db_session
@app.route("/tickets", methods=["GET"])
def get_tickets():
    data = []
    with db_session:
        for d in db.Ticket.select():
            if not d.paid:
                d.set(duration=int(((datetime.datetime.utcnow() - d.start).seconds / 3600 ) + 0.5))
        data = [d for d in db.Ticket.select()]
    return jsonify({
        "ticket": data if data else []
    })


@db_session
@app.route("/tickets", methods=["POST"])
def create_ticket():
    data = request.get_json()
    print(data)
    data = data['ticket']
    with db_session:
        id = db.db.insert("ticket", start=datetime.datetime.utcnow(), numplate=data['numplate'],paid=False ,returning='id')
    return jsonify({
        "ticket": {
            "id": id
        }
    })


@db_session
@app.route("/tickets/<int:ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    data = {}
    with db_session:
        for d in db.Ticket.select():
            if d.id == ticket_id:
                data = d
                if not d.paid:
                    d.set(duration=int(((datetime.datetime.utcnow() - d.start).seconds / 3600 ) + 0.5))
                break
    return jsonify({
        "ticket": data if data else {}
    })

@db_session
@app.route("/tickets/<int:ticket_id>", methods=["PUT"])
def update_ticket(ticket_id):
    data = request.get_json()
    data = data['ticket']
    with db_session:
        db.Ticket[ticket_id].set(paid=data['paid'])
    return "{}"

@db_session
@app.route("/tickets/<int:ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    with db_session:
        db.Ticket[ticket_id].delete()
    return "{}"
