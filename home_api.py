from home_manager import HomeManager
from flask import Flask, request
from condo import Condo
from detached_home import DetachedHome
import json

app = Flask(__name__)

filepath = 'home_records.txt'
example = HomeManager(filepath)

# API Methods are below this line

#works screens taken
@app.route('/homemanager/homes', methods=['POST'])
def add_home():
    """ Adds a home to the HomeManager """
    content = request.json

    try:
        if content["type"] == "detached home":
            det = DetachedHome(content['square_feet'], content['year_built'], content['number_of_rooms'],
                        content['number_of_bathrooms'], content['city'], content['selling_agent'], content['yearly_property_tax'],
                        content['number_of_floors'], content['has_rental_suite'])
            example.add_home(det)

        elif content["type"] == "condo":
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

@app.route('/homemanager/homes/<int:id>', methods=['PUT'])
def update_home(id):
    """ Update a Home by ID """
    content = request.json
    if example.get_home_by_id(id) is None:
        response = app.response_class(
            response="Home doesn't exist",
            status=404
        )
        return response
    try:
        if content["type"] == "detached home":
            det = DetachedHome(content['square_feet'], content['year_built'], content['number_of_rooms'],
                        content['number_of_bathrooms'], content['city'], content['selling_agent'], content['yearly_property_tax'],
                        content['number_of_floors'], content['has_rental_suite'])
            det.set_id(id)
            example.update_home(det)

        elif content["type"] == "condo":
            con = Condo(content['square_feet'], content['year_built'], content['number_of_rooms'],
                        content['number_of_bathrooms'], content['city'], content['selling_agent'], content['yearly_property_tax'],
                        content['monthly_strata_fee'], content['pets_allowed'])
            con.set_id(id)
            example.update_home(con)


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
        example.delete_home(id)

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

@app.route('/homemanager/homes/<int:id>', methods=['GET'])
def get_home(id):
    """ Get a single existing Home based on ID """
    try:
        home = example.get_home_by_id(id)
        if home is not None:
            response = app.response_class(
            status=200,
            response=json.dumps(home.to_dict()),
            mimetype='application/json'
            )
        else:
            response = app.response_class(
            response="Home with given ID does not exist.",
            status=404
            )
        return response    
    except ValueError as e:
        response = app.response_class(
        response=str(e),
        status=400
        )
        return response

@app.route('/homemanager/homes/all', methods=['GET'])
def get_all_homes():
    """ Returns all homes in an inventory manager """
    all_homes = example.get_all_homes()
    dicted = list()
    for home in all_homes:
        dicted.append(home.to_dict())

    response = app.response_class(
        status=200,
        response=json.dumps(dicted),
        mimetype='applications/json'
    )
    return response

@app.route('/homemanager/homes/all/<string:type>', methods=['GET'])
def get_homes_by_type(type):
    """ Returns all homes of a certain type """
    try:
        homes_by_type = example.get_all_homes_by_type(type)
        dicted = list()
        for home in homes_by_type:
            dicted.append(home.to_dict())
        response = app.response_class(
            status=200,
            response=json.dumps(dicted),
            mimetype='applications/json'
        )   
        return response

    except ValueError as e:
        response = app.response_class(
            response=str("Type is not valid"),
            status=400
        )
        return response

@app.route('/homemanager/homes/stats', methods=['GET'])
def get_home_stats():
    """ Gets the Listing Stats for the HomeManager """
    listing_stats = example.get_listing_stats()
    response = app.response_class(
        status=200,
        response=json.dumps(listing_stats.to_dict()),
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run()