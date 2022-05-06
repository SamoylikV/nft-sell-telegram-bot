from flask import Flask
from flask_restful import Api, Resource
import __init__
from consts import PSQL_ADDRESS, PSQL_PASSWORD, PSQL_PORT, PSQL_DBNAME, PSQL_USERNAME

print(PSQL_PORT)
app = Flask(__name__)
api = Api(app)
conn = __init__.connect(user=PSQL_USERNAME, dbname=PSQL_DBNAME, password=PSQL_PASSWORD, host=PSQL_ADDRESS, port=PSQL_PORT)

print(123)

class Quantum(Resource):
    def get(self, id=0):
        return __init__.get_quantum_by_id(conn, id)

    def post(self, quant):
        __init__.create_quantum(conn, quant)

    def delete(self, id):
        __init__.delete_quantum(conn, id)
        return f"{__init__.get_quantum_by_id_api(conn, id)} removed", 200


class News(Resource):
    def get(self, n=1):
        return __init__.get_latest_n_news(conn, n)

    def post(self, news):
        __init__.create_news(conn, news)


class Events(Resource):
    def get(self):
        return __init__.get_latest_events(conn)

    def post(self, event):
        __init__.create_event(conn, event)

    def delete(self, id):
        __init__.delete_quantum(conn, id)
        return f"{__init__.get_quantum_by_id_api(conn, id)} removed", 200


class Tutor(Resource):
    def get(self, id=0):
        return __init__.get_tutor_by_id(conn, id)


api.add_resource(Quantum, "/quant", "/quant/", "/quant/<int:id>")
api.add_resource(News, "/news", "/news/", "/news/<int:id>")
api.add_resource(Events, "/event", "/event/", "/event/<int:id>")
api.add_resource(Tutor, "/tutor", "/tutor/", "/tutor/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
