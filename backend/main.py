import db
import server
from pony.orm import commit


db.connect()
server.app.run()
