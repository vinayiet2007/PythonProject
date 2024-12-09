from common.utilities.logger import Logger
def test_get_request(set_api_client):
    api_client = set_api_client
    response = api_client.get_request("?name=michael")
    Logger.info(response)
    print(f"{response}")