from Regression.RestAPI import RestAPI
class RestAPI():
    """Keywords to implement our REST API framework for our automation"""# from Regression.MappingRegession import Mapping

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    rest_client = RestAPI()
    def get(self, url):
        self.rest_client.get_request(url)
    def post(self, url):
        self.rest_client.post_request(url)
    def delete(self, url, name):
        self.rest_client.delete_request(url, name)