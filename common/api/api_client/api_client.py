import requests

class APIClient:

    def __init__(self,base_url):
        self.base_url = base_url
        pass

    def get_request(self,rest_url):
        response = requests.get(f"{self.base_url}{rest_url}")
        return response.json()

    def post_request(self,rest_url,payload,header):
        response = requests.post(self.base_url+rest_url,data=payload,headers=header)
        return response.json()

    def put_request(self,rest_url,payload,header):
        response = requests.put(self.base_url+rest_url,data=payload,headers=header)
        return response.json()