from urllib import request
import json

ur = 'http://127.0.0.1:5000/api/films'


def test_get():
    req = request.Request(ur)
    res = request.urlopen(req)
    print(res.read().decode())


def test_post():
    data = {
        "title": "Forrest Gump",
        "length": 8520,
        "year": 1994,
        "director": "Robert Zemeckis",
        "actors": [
            {"name": "Tom Hanks"},
            {"name": "Robin Wright"},
            {"name": "Gary Sinise"},
            {"name": "Mykelti Williamson"},
            {"name": "Sally Field"},
            {"name": "Michael Conner Humphreys"}
        ]
    }
    req = request.Request(ur)
    req.add_header('Content-Type', 'application/json')
    jsondata = json.dumps(data)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    res = request.urlopen(req, data=jsondataasbytes)
    print(res.read().decode())


# test_get()
# test_post()
