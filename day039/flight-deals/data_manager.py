import requests

sheety_endpoint = "https://api.sheety.co/a72fb3c79b3dabb89545d0ff6200f208/flightDeals/prices"
sheety_headers = {
    "Content-Type": "application/json",
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)
