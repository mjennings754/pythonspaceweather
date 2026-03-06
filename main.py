import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def get_k_index():
    request_type = "get-k-index"
    url = f"https://sws-data.sws.bom.gov.au/api/v1/{request_type}"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    requestBody = {
        'api_key': api_key,
        'options': { 'location': 'Australian region'}}
    
    response = requests.post(url, headers=headers, json=requestBody)

    check_response(response, "k")


def get_a_index():
    request_type = "get-a-index"
    url = f"https://sws-data.sws.bom.gov.au/api/v1/{request_type}"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    requestBody = {
        'api_key': api_key,
        'options': { 'location': 'Australian region'}}
    
    response = requests.post(url, headers=headers, json=requestBody)

    check_response(response, "a")


def check_response(response, index_type):
    if response.status_code == 200:
        responseBody = response.json()
        data = responseBody['data']

        if index_type == "k":
            index_value = data[0]['index']
            valid_time = data[0]['valid_time']
            description = k_index_description(index_value)
            print(f"K Index (geomagnetic activity (short-term)): {index_value} ({description})")
        elif index_type == "a":
            index_value = data[0][0]['index']
            valid_time = data[0][0]['valid_time']
            description = a_index_description(index_value)
            print(f"A Index (geomagnetic activity (long-term)): {index_value} ({description})")

        print(f"Valid time: {valid_time}")
    else:
        responseBody = response.json()
        errors = responseBody['errors']
        print(errors)

def k_index_description(k):
    k = int(k)

    if k <= 1:
        return "Very quiet"
    elif k == 2:
        return "Quiet"
    elif k == 3:
        return "Unsettled"
    elif k == 4:
        return "Active"
    elif k == 5:
        return "Minor storm"
    elif k == 6:
        return "Moderate storm"
    elif k == 7:
        return "Strong storm"
    elif k == 8:
        return "Severse storm"
    else:
        return "Extreme storm"
    
def a_index_description(a):
    a = int(a)

    if a <= 7:
        return "Quiet"
    elif a <= 15:
        return "Unsettled"
    elif a <= 29:
        return "Active"
    elif a <= 49:
        return "Minor storm"
    elif a <= 99:
        return "Major storm"
    else:
        return "Severe storm"



get_k_index()
get_a_index()