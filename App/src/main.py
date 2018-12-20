from flask import Flask, jsonify, request
from flask_cors import CORS
from .entidades.entidades import Session, engine, Base
from .entidades.ejemplo import Thing, ThingSchema

# creating the Flask application
app = Flask(__name__)

CORS(app)  # allows CORS for all domains on all routes

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/exam')
def get_things():
    # fetching from the database
    session = Session()
    thing_objects = session.query(Thing).all()

    # transforming into JSON-serializable objects
    schema = ThingSchema(many=True)
    things = schema.dump(thing_objects)

    # serializing as JSON
    session.close()
    return jsonify(things.data)


@app.route('/exam', methods=['POST'])
def add_thing():
    # mount thing object
    posted_thing = ThingSchema(only=('title','description')).load(request.get_json())
    thing = Thing(**posted_thing.data,created_by="HTTP post request")

    # persist thing
    session = Session()
    session.add(thing)
    session.commit()

    # return created thing
    new_thing = ThingSchema().dump(thing).data
    session.close()
    return jsonify(new_thing), 201