"""test module for course1_solution.py"""

import pytest
import json
from flask import jsonify


from solutions import course3_solution, awesome_dictionary_to_return


@pytest.fixture
def test_client():
    """configure app and get client for testing"""
    course3_solution.app.config['TESTING'] = True
    client = course3_solution.app.test_client()
    yield client


def test_jsonify_get(test_client):
    """test for the GET /jsonify endpoint"""

    url = '/jsonify'
    response = test_client.get(url)
    assert response.json == awesome_dictionary_to_return
    assert response.status_code == 200


def test_jsonify_post(test_client):
    """test for the POST /jsonify endpoint"""

    url = '/jsonify'
    body = {'Original request': 'This is the original request'}

    expected_response = dict.copy(awesome_dictionary_to_return)
    expected_response['Original request'] = 'This is the original request'
    response = test_client.post(url, json=body)
    assert response.json == expected_response
    assert response.status_code == 200


def test_jsonify_post_invalid_should_return_400(test_client):
    """test for the POST /jsonify endpoint"""

    url = '/jsonify'
    body = {'Original reques': 'This is the original request'}

    expected_response = dict.copy(awesome_dictionary_to_return)
    expected_response['Original request'] = 'This is the original request'
    response = test_client.post(url, json=body)
    assert response.status_code == 400


