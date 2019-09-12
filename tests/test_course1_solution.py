"""test module for course1_solution.py"""

import pytest

from solutions import course1_solution


@pytest.fixture
def test_client():
    """configure app and get client for testing"""
    course1_solution.app.config['TESTING'] = True
    client = course1_solution.app.test_client()

    return client


def test_question_1(test_client):
    """test for the /myname endpoint"""
    response = test_client.get('/myname')
    assert response.data == b'"My name is Wietse!"\n'


def test_question_2(test_client):
    """test for the /mynameUppercase endpoint"""
    response = test_client.get('/mynameUppercase')
    assert response.data == b'"MY NAME IS WIETSE!"\n'


def test_question_3(test_client):
    """test for the /concattedStrings endpoint"""
    response = test_client.get('/concattedStrings')
    assert response.data == b'"My name is Wietse!MY NAME IS WIETSE!"\n'
