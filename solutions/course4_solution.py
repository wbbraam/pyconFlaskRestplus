"""Module for the solutions of course4.py"""

import os
import csv

from flask import jsonify, request
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest

from solutions import create_api, create_app, mainTitle, course4_field_names

app = create_app()  # pylint: disable=invalid-name
api = create_api(app, mainTitle, 'Description')  # pylint: disable=invalid-name

CSV_FILE_NAME = '/../example.csv'


@api.route('/employee/<string:employee_id>')
class Csv(Resource):
    """Class for the employee API"""
    @staticmethod
    def get(employee_id):
        """GET endpoint for retrieving employee info with the given employee_id"""
        try:
            return jsonify(retrieve_employee_with_id(employee_id))
        except KeyError:
            raise BadRequest

    @staticmethod
    def put(employee_id):
        """PUT endpoint for modifying the employee info with the given employee_id"""
        if check_if_record_is_there(employee_id):
            update_employee_with_id(employee_id, request.json)
        else:
            raise BadRequest

    @staticmethod
    def delete(employee_id):
        """DELETE endpoint for deleting the employee info with the given employee_id"""
        try:
            delete_employee_with_id(employee_id)
        except KeyError:
            raise BadRequest


@api.route('/employee')
class Csv2(Resource):
    """Class for the employee API without employee_id"""
    @staticmethod
    def get():
        """GET endpoint for fetching all employee records"""
        list_employees = list(read_data_from_csv(CSV_FILE_NAME).values())
        return jsonify(list_employees)

    @staticmethod
    def post():
        """POST endpoint for adding new employee info"""
        data = request.json
        if not check_if_record_is_there(data['Employee ID']):
            add_employee_data(request.json)
        else:
            raise BadRequest


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
    write_data_to_csv(CSV_FILE_NAME, data, 'r+', True, course4_field_names)


def add_employee_data(data):
    """Function to add employee info to example.csv file using the employee info provided"""
    write_data_to_csv(CSV_FILE_NAME, data, 'a', False, course4_field_names)


def delete_employee_with_id(employee_id):
    """Function to delete employee info from example.csv file using the given employee_id"""
    data = read_data_from_csv(CSV_FILE_NAME)
    if employee_id in data:
        del data[employee_id]
    write_data_to_csv(CSV_FILE_NAME, data, 'r+', True, course4_field_names)


def read_data_from_csv(file_name):
    """Function to read csv data from the given file"""
    data = dict()
    with open(os.path.dirname(__file__) + file_name, encoding='utf-8-sig') as csv_file:
        input_file = csv.DictReader(csv_file)
        for row in input_file:
            print(row)
            data[row['Employee ID']] = row
    csv_file.close()
    return data


def write_data_to_csv(file_name, data, mode, is_rows, fieldnames):
    """Function to write data to the given file. is_rows parameter
       is provided to write multiple rows of data"""
    with open(os.path.dirname(__file__) + file_name, mode=mode) as csv_file:
        csv_writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
        if mode == 'r+':
            print('mode is {0}'.format('delete'))
            csv_file.truncate(0)
            csv_writer.writeheader()
        if is_rows:
            for value in data.values():
                csv_writer.writerow(value)
        else:
            csv_writer.writerow(data)
    csv_file.close()


def check_if_record_is_there(employee_id):
    """Function to check if an employee record exists for the given employee id"""
    data = read_data_from_csv(CSV_FILE_NAME)
    if str(employee_id) in data:
        print('True')
        return True
    return False


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=PORT)
