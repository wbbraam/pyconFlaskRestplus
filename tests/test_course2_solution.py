"""test module for course1_solution.py"""

import pytest

from solutions import course2_solution


@pytest.fixture
def test_client():
    """configure app and get client for testing"""
    course2_solution.app.config['TESTING'] = True
    client = course2_solution.app.test_client()
    yield client


def test_sum_with_valid_input_should_return_ok(test_client):
    """test for the /sum endpoint with valid params"""

    url = '/sum?value1={0}&value2={1}'.format(1, 2)
    response = test_client.get(url)
    assert response.data == b'3\n'
    assert response.status_code == 200


def test_sum_with_invalid_input_should_return_bad_request(test_client):
    """test for the /sum endpoint with invalid param"""

    url = '/sum?value={0}&value2={1}'.format(1, 2)
    response = test_client.get(url)
    assert response.status_code == 400


def test_compute_add(test_client):
    """test for the /compute/add endpoint"""

    data = {'value1': 1, 'value2': 2}
    url = '/compute/add'
    response = test_client.post(url, json=data)
    assert response.status_code == 200
    assert response.data == b'3\n'


def test_compute_subtract(test_client):
    """test for the /compute/subtract endpoint"""

    data = {'value1': 5, 'value2': 3}
    url = '/compute/subtract'
    response = test_client.post(url, json=data)
    assert response.status_code == 200
    assert response.data == b'2\n'


def test_compute_multiply(test_client):
    """test for the /compute/multiply endpoint"""

    data = {'value1': 5, 'value2': 3}
    url = '/compute/multiply'
    response = test_client.post(url, json=data)
    assert response.status_code == 200
    assert response.data == b'15\n'


def test_compute_divide(test_client):
    """test for the /compute/divide endpoint"""

    data = {'value1': 6, 'value2': 3}
    url = '/compute/divide'
    response = test_client.post(url, json=data)
    assert response.status_code == 200
    assert response.data == b'2.0\n'


def test_compute_compute_bad_request(test_client):
    """test for the /compute endpoint with invalid param"""

    data = {'value': 6, 'value2': 3}
    url = '/compute/divide'
    response = test_client.post(url, json=data)
    assert response.status_code == 400


def test_compute_compute_bad_request_divide_by_zero(test_client):
    """test for the /compute endpoint corner case"""

    data = {'value1': 6, 'value2': 0}
    url = '/compute/divide'
    response = test_client.post(url, json=data)
    assert response.status_code == 400
