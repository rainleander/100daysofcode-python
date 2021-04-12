import requests
from datetime import datetime

USERNAME = "rain"
TOKEN = "thisisasecret123"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # create user account [https://docs.pixe.la/entry/post-user]
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# # create a graph [https://docs.pixe.la/entry/post-graph]
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")

pixel_params = {
    "date": formatted_today,
    "quantity": "45",
}

# # post a pixel [https://docs.pixe.la/entry/post-pixel]
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_params = {
    "quantity": "240",
}

# # update a pixel [https://docs.pixe.la/entry/put-pixel]
# response = requests.put(url=f"{pixel_endpoint}/{formatted_today}", json=update_params, headers=headers)
# print(response.text)

# delete a pixel [https://docs.pixe.la/entry/delete-pixel]
response = requests.delete(url=f"{pixel_endpoint}/20200412", headers=headers)
print(response.text)
