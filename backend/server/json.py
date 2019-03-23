from flask.json import JSONEncoder
from pony.orm.core import Entity


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Entity):
            return obj.to_json()
        return JSONEncoder.default(self, obj)
