"""Module for the solutions of course4.py"""

import os
import csv

from flask import jsonify, request
from flask_restplus import Resource

from solutions import create_api, create_app, mainTitle

app = create_app()  # pylint: disable=invalid-name
api = create_api(app, mainTitle, 'Description')  # pylint: disable=invalid-name

CSV_FILE_NAME = 'example.csv'


@api.route('/employee/<string:employee_id>')
class Csv(Resource):
    """Class for the employee API"""
    @staticmethod
    def get(employee_id):
        """GET endpoint for retrieving employee info with the given employee_id"""
        return jsonify(retrieve_employee_with_id(employee_id))

    @staticmethod
    def put(employee_id):
        """PUT endpoint for modifying the employee info with the given employee_id"""
        update_employee_with_id(employee_id, request.json)

    @staticmethod
    def post():
        """POST endpoint for adding new employee info"""
        add_employee_data(request.json)

    @staticmethod
    def delete(employee_id):
        """DELETE endpoint for deleting the employee info with the given employee_id"""
        delete_employee_with_id(employee_id)


def retrieve_employee_with_id(employee_id):
    """Function to retrieve employee info from example.csv file using the given employee_id"""
    data = read_data_from_csv(CSV_FILE_NAME)
    return data[employee_id]


def update_employee_with_id(employee_id, new_employee):
    """Function to update employee info from example.csv file using
       the given employee_id and new employee info"""
    data = read_data_from_csv(CSV_FILE_NAME)
    if employee_id in data:
        data[employee_id] = new_employee
    write_data_to_csv(CSV_FILE_NAME, data, 'r+', True)


def add_employee_data(data):
    """Function to add employee info to example.csv file using the employee info provided"""
    write_data_to_csv(CSV_FILE_NAME, data, 'a', False)


def delete_employee_with_id(employee_id):
    """Function to delete employee info from example.csv file using the given employee_id"""
    data = read_data_from_csv(CSV_FILE_NAME)
    if employee_id in data:
        del data[employee_id]
    write_data_to_csv(CSV_FILE_NAME, data, 'r+', True)


def read_data_from_csv(file_name):
    """Function to read csv data from the given file"""
    data = dict()
    with open(file_name, encoding='utf-8-sig') as csv_file:
        input_file = csv.DictReader(csv_file)
        for row in input_file:
            data[row['Employee ID']] = row
    csv_file.close()
    return data


def write_data_to_csv(file_name, data, mode, is_rows):
    """Function to write data to the given file. is_rows parameter
       is provided to write multiple rows of data"""
    with open(file_name, mode=mode) as csv_file:
        csv_writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=['Employee ID', 'Name'])
        if mode == 'r+':
            print('mode is {0}'.format('delete'))
            csv_file.truncate(0)
            csv_writer.writeheader()
        if is_rows:
            for key, value in data.items():
                csv_writer.writerow(value)
        else:
            csv_writer.writerow(data)
    csv_file.close()


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=PORT)
