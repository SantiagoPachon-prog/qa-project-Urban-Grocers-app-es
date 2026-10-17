import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = body,
                         headers = data.headers)

response1 = post_new_user(data.user_body)

print(response1.status_code)


def post_new_client_kit(kit_body, auth_token):
    current_header = data.headers.copy()
    current_header["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                  json= kit_body,
                  headers= current_header)

response = post_new_client_kit(data.kit_body, response1.json()["authToken"])
print(response.text)
