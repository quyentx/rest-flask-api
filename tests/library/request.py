import requests
import allure

@allure.step('REQUEST')
def send_request(method, url, headers = {}, body={}):
    if method == 'GET':
        response = requests.get(url, headers=headers)
        allure.attach(response.content, 'RESPONSE', allure.attachment_type.JSON)
        return response
    
    if method == 'POST':
        response = requests.post(url, headers=headers, data=body)
        allure.attach(response.content, 'RESPONSE', allure.attachment_type.JSON)
        return response

    raise Exception('Method not found: ' + method)