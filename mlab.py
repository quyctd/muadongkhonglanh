import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds021046.mlab.com:21046/warmwinter
host = "ds021046.mlab.com"
port = 21046
db_name = "warmwinter"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
