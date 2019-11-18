from home_manager import HomeManager
from flask import Flask, request
from condo import Condo
from detached_home import DetachedHome
import json

app = Flask(__name__)

filepath = ''
example = HomeManager()

# API Methods are below this line

#works screens taken
@app.route('/homemanager/homes', methods=['POST'])
def add_home():
    """ Adds a home to the HomeManager """
    content = request.json

    try:
        if content["type"] == "Detached Home":
            det = DetachedHome(content['square_feet'], content['year_built'], content['number_of_rooms'],
                        content['number_of_bathrooms'], content['city'], content['selling_agent'], content['yearly_property_tax'],
                        content['number_of_floors'], content['has_rental_suite'])
            example.add_home(det)

        elif content["type"] == "Condo":
            con = Condo(content['square_feet'], content['year_built'], content['number_of_rooms'],
                        content['number_of_bathrooms'], content['city'], content['selling_agent'], content['yearly_property_tax'],
                        content['monthly_strata_fee'], content['pets_allowed'])
            example.add_home(con)


        else:
            response = app.response_class(
                response="Unsupported home type",
                status=400
            )
            return response

        response = app.response_class(
            status=200
        )
        return response

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
        return response

#works screenshots taken
@app.route('/homemanager/homes/<int:id>', methods=['DELETE'])
def delete_home(id):
    """ Delete a home from the HomeManager """

    try:
        home = example.delete_home(id)

        response = app.response_class(
            status=200
            )
        return response

    except ValueError as e:
        response = app.response_class(
            response=str("Home doesn't exist"),
            status=404
        )
        return response

@app.route('/homemanager/homes/all', methods=['GET'])
def get_all_homes():
    """ Returns all homes in an inventory manager """
    all_homes = example.get_all_homes()
    dicted = all_homes.to_dict()

    response = app.response_class(
        status=200,
        response=json.dumps(dicted),
        mimetype='applications/json'
    )
    return response

@app.route('/homemanager/homes/all/<string:type>', methods=['GET'])
def get_description(type):
    """ Returns all homes of a certain type """
    homes_by_type = example.get_all_homes_by_type(type)

    try:
        response = app.response_class(
            status=200,
            response=json.dumps(homes_by_type),
            mimetype='applications/json'
        )
        return response

    except ValueError as e:
        response = app.response_class(
            response=str("Type is not valid"),
            status=404
        )
        return response

if __name__ == "__main__":
    app.run()