import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
response.raise_for_status()

"""
1xx: hold on
2xx: here you go
3xx: go away
4xx: you screwed up
5xx: i (the server) screwed up
"""
data = response.json()
# {'iss_position': {'longitude': '74.1416', 'latitude': '4.4747'}, 'message': 'success', 'timestamp': 1614750671}
print(data)
data = response.json()["iss_position"]
# {'longitude': '74.1416', 'latitude': '4.4747'}
print(data)
data = response.json()["iss_position"]["latitude"]
# 4.4747
print(data)
