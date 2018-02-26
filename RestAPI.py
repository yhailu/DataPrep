import requests
#from BaseClasses.singleton import Driver
from selenium.webdriver.common.by import By
import time
import json
import urllib3

class RestAPI():
    """

    **REST API Automation Framework for VE Field Development**

    """

    def __init__(self):
        """**Set up environment for test execution**"""

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        requests.packages.urllib3.disable_warnings()
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        try:
            requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
        except AttributeError:
            # no pyopenssl support used / needed / available
            pass
        self.base_url = "https://vebd1.vertexinc.com/vertex/open-ws/veit/vebd/"

        self.username = 'vedemo'
        self.password = 'iL0veTax'

        self.payload = "{\"name\":\"appTest\"," \
              "\"widgets\":[{\"additionalProperties\":{}," \
              "\"name\":\"appTest\",\"sizeX\":2,\"sizeY\":2,\"col\":0,\"row\":0}]," \
              "\"additionalProperties\":{\"defaultDash\":\"NO\"}}"

        self.error = False #lets us know if error has occured during request
        self.headers = {}  #holds custom headers
        self.session = None
        self.auth_cookies = {}



    def base_url(self):
        """
        **Summary**:
        Deprecated method will remove in future after payload generator class is created

        Returns: Returns base url if we ever need it

        """
        url = self.base_url
        return url

    def print_json(self, request):
        """
        **Summary**: prints json from request object we pass in

        Args:
            :request: request object

        Returns: Void

        """
        """
        Prints status and text of response"""
        print("Status: " + str(request.status_code))
        print("ResponseText: " + request.text)

    def status_handler(self, request):
        """
        **Summary**:
        If this method receives a bad status code it will throw an exception letting us know
        something went wrong.

        Args:
            :request: a request object from requests library


        Returns: void

        """
        assert request.status_code in [200, 201, 202, 204, 304],"Expected no error (http status code 2xx), bot got " + \
            str(self.request.status_code) + ": " + str(self.request.text)

    def json_handler(self, unparsed_json, name):
        """
        **Summary**: parses json and returns id of element we want

        Args:
            :unparsed_json: json sent back from server
            :name: name of object in our application that we want

        Returns: If finds object we are looking for, a mongo object id will be returned

        """
        parsed_json = json.loads(unparsed_json)
        for dashboard in parsed_json:
            if dashboard['name'] == name:
                return (dashboard['id'])

        # print("json id" + parsed_json[2]['id'])
        # return parsed_json[2]['id']
        # print('josn id2' +  parsed_json[1]['id'])

    def get_request(self, url):
        """
        Summary: send GET request from requests library

        Args:
            url: Web Service call url

        Returns: void

        """

        self.request = ''
        headers = {'Content-Type' : "application/json",
                   'accept':"application/json",
        }


        while self.request == '':
            try:
                self.request = requests.get(self.base_url + url, headers=headers, auth=(self.username, self.password), verify=False)
                print(self.request.status_code)
                print(self.request.headers)
                print("json: "+self.request.text)
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue
        self.status_handler(self.request)
       # self.print_json(self.request)

    def post_request(self, url):
        """
        **Summary**:
        Handles POST method call

        Args:
            :url: Web service url that we want to post

        Returns: void, unless something went wrong then exception is thrown

        """
        self.request = requests.post(self.base_url + url, data = self.payload, auth = (self.username, self.password), verify = False)
        self.status_handler(self.request)

        if str(self.request.status_code) != "201":
            print("Status: "+ str(self.request.status_code))

            raise ValueError('wrong status code was returned: ' + str(self.request.status_code))
        else:
            print('Creation was Successful')

    def get_id(self, url, name):
        """
        **Summary**:
        Will get  the id of name of the element we want through means of GET method

        Args:
            :url: Web service url
            :name: name of object we want to get id of

        Returns: id as an integer

        """
        self.request = requests.get(self.base_url + url, auth=(self.username, self.password), verify = False)
        print(self.request.status_code)
        self.status_handler(self.request)
        print(self.request.text)
        id = self.json_handler(self.request.text, name)
        print(id)
        return id

    def delete_request(self, url, name):
        """
        **Summary**:
        Handles DELETE method

        Args::
            :url: Web service url
            :name: name of object that we want to delete

        Returns: Void

        """
        id = self.get_id(url, name)
        self.request = requests.delete(self.base_url+ url + "/"+ id, auth = (self.username, self.password), verify = False)
        self.status_handler(self.request)



if __name__=="__main__":
    r = RestAPI()
    # r.post_request('dashboards')
    # r.get_request('tablemap2s')
    # r.get_request('querys')
    # r.get_request('joins')
    # r.delete_request('unions', 'autounion1')
    # r.delete_request('dataflows', 'bert')
    # r.delete_request('dashboards', 'srimanueltest123')
    r.get_request('dashboards')
