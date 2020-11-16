import sys
import psycopg2
import logging
from flask import Flask
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

# abort(404, message="something weird happened".format(starship_id))

parser = reqparse.RequestParser()
parser.add_argument('starship_object')

def getConnection():

    t_host     = "localhost"
    t_port     = "5432" # default postgres port
    t_dbname   = "starship_db"
    t_user     = "jasonwer"
    t_password = "jasonwer"

    c = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_password)
    return c


class StarShip(Resource):
    def get(self, starship_id):
        c = getConnection()
        cur = c.cursor(cursor_factory=RealDictCursor)
        sql = """SELECT * FROM starships WHERE TRIM(registry) = '""" + starship_id + """' ;"""
        cur.execute(sql)
        res = cur.fetchall()
        if cur.rowcount = 0:
            logging.info("Starship record with id " + starship_id + " does not exist. No record returned.")
        else:
            logging.info("Starship record with id " + starship_id + " returned.")
        return res
            

class StarShipList(Resource):
    def get(self):
        c = getConnection()
        cur = c.cursor(cursor_factory=RealDictCursor)
        sql = """SELECT * FROM starships;"""
        cur.execute(sql)
        res = cur.fetchall()
        if cur.rowcount = 0:
            logging.warning("No starship records exist. Have you loaded the data?")
        else:
            logging.info("Starship listing returned")
        return res

try:
    ######################
    api.add_resource(StarShipList, '/api/v1/starships')
    api.add_resource(StarShip, '/api/v1/starship/<string:starship_id>')
    ###########################

    if __name__ == "__main__":
        app.run(host='0.0.0.0',port=5500, threaded=True)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    logging.error(f'Error {e}')
    sys.exit(1)

except IOError as e:

    print(f'Error {e}')
    logging.error(f'Error {e}')
    sys.exit(1)

finally:

    print("Done.")
