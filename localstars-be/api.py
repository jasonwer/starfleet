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

# abort(404, message="something weird happened".format(star_id))

parser = reqparse.RequestParser()
parser.add_argument('star_object')

def getConnection():

    t_host     = "localhost"
    t_port     = "5432" # default postgres port
    t_dbname   = "localstars_db"
    t_user     = "jasonwer"
    t_password = "jasonwer"

    c = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_password)
    return c


class Star(Resource):
    def get(self, star_id):
        c = getConnection()
        cur = c.cursor(cursor_factory=RealDictCursor)
        sql = """SELECT name, common_name, spectral_type, mass,distance_ly FROM localstars WHERE name = """ + star_id + """ ;"""
        cur.execute(sql)
        res = cur.fetchall()
        if cur.rowcount = 0:
            logging.info("Star record with id " + star_id + " does not exist. No record returned.")
        else:
            logging.info("Star record with id " + star_id + " returned.")
        return res
            

class StarList(Resource):
    def get(self):
        c = getConnection()
        cur = c.cursor(cursor_factory=RealDictCursor)
        sql = """SELECT name, common_name, spectral_type, mass,distance_ly FROM localstars;"""
        cur.execute(sql)
        res = cur.fetchall()
        if cur.rowcount = 0:
            logging.warning("No star records exist. Have you loaded the data?")
        else:
            logging.info("Star listing returned")
        return res

try:
    ######################3
    api.add_resource(StarList, '/api/v1/localstars')
    api.add_resource(Star, '/api/v1/localstar/<star_id>')
    ###########################3

    if __name__ == "__main__":
        app.run(host='0.0.0.0',port=5501, threaded=True)

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
