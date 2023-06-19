from library import request
import allure
import pytest

def test_record_income(base_url):
    with allure.step('Send POST request to record new income'):
        headers = {'Content-Type': 'application/json'}
        body = """{
            "amount": 300.0,
            "description": "loan payment"
            }"""
        response = request.send_request('POST', f"{base_url}/incomes", headers, body)
        assert response.status_code == 204


def test_get_incomes(base_url):
    with allure.step('Send GET request to get list of incomes'):
        headers = {}
        response = request.send_request('GET', f"{base_url}/incomes", headers)
        assert response.status_code == 200