import os, time, datetime
from pony import orm


db = orm.Database()
try:
    url = os.environ['DATABASE_URL']
except:
    url = "postgres://postgres:postgres@localhost:5432/CarPark"

def connect():
    db.bind("postgres", url)
    db.generate_mapping(create_tables=True)


class CarPark(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)
    capacity = orm.Required(int)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "capacity": self.capacity
        }


class HappyHour(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    happyhour = orm.Required(str)

    def to_json(self):
        return {
            "id": self.id,
            "happyhour": self.happyhour
        }

class Price(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    price = orm.Required(str)

    def to_json(self):
        return {
            "id": self.id,
            "price": self.price
        }



class Ticket(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    start = orm.Required(datetime.datetime)
    numplate = orm.Required(str, unique=True)
    duration = orm.Optional(int)
    paid = orm.Required(bool, default=False)

    def to_json(self):
        return {
            "id": self.id,
            "start": self.start,
            "numplate": self.numplate,
            "duration": self.duration,
            "paid": self.paid
        }
