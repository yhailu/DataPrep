import requests
from pprint import pprint
import json

if __name__=='__main__':

    def getDashboards():
        url = "https://vebd1.vertexinc.com/vertex/open-ws/veit/vebd/appconfiges/app"

        response = requests.get(url, auth = ('vedemo', 'iL0veTax'), verify = False)

        print("status of get dashboards", response.status_code)
        # print(response.text)
        # print('status of dashboards call:', response.headers)
        # print("dictionary of cookies: ", response.cookies)

    def create():
        url = "https://vebd1.vertexinc.com/vertex/open-ws/veit/vebd/dashboards"
        payload = "{\"name\":\"DashboardTest\",\"widgets\":[{\"XAxisCategories\":null,\"XAxisTitleText\":null,\"YAxisTitleText\":null,\"YAxisType\":null,\"additionalProperties\":{\"boxValue\":\"Sno\",\"boxColName\":\"int1\",\"decimalSeries\":[{\"dColName\":\"\",\"dColCheck\":false}],\"newSeries\":[]},\"col\":0,\"id_\":null,\"name\":\"New Widget\",\"query\":\"59fb8371e4b0ce82188a4eeb\",\"row\":0,\"selectedMapCol\":null,\"selectedSeries\":[],\"sizeX\":2,\"sizeY\":2,\"template\":\"box\"}],\"additionalProperties\":{\"defaultDash\":\"NO\"}}"
        headers = {
            'origin': "https://vebd1.vertexinc.com",
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            'content-type': "application/json;charset=UTF-8",
            'accept': "*/*",
            'referer': "https://vebd1.vertexinc.com/vertex/open/veit/index.html",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.9",
            'cookie': "JSESSIONID=1fe48076hudq0vfghnwu62loc; _ga=GA1.2.819411697.1495725341; betatester=yes; netuser=yhailu; JSESSIONID=1fe48076hudq0vfghnwu62loc; _ga=GA1.2.819411697.1495725341; betatester=yes; netuser=yhailu",
            'cache-control': "no-cache",
            'postman-token': "53e30de3-2f4b-670f-f8ba-94386f1b30ba"
        }

        createADashboard = requests.post(url, data=payload, headers=headers)

        print ('CREATION: ', createADashboard.status_code)

    def remove():
        url = "https://vebd1.vertexinc.com/vertex/open-ws/veit/vebd/dashboards/5a154c2ce4b069c686bd4513"

        headers = {
                'accept': "application/json, text/plain, */*",
                'origin': "https://vebd1.vertexinc.com",
                'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
                'referer': "https://vebd1.vertexinc.com/vertex/open/veit/index.html",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cookie': "JSESSIONID=qnnmtrv4eyg4hu3j6luh60rg; _ga=GA1.2.819411697.1495725341; betatester=yes; netuser=yhailu",
                'cache-control': "no-cache",
                'postman-token': "1780e657-eef6-5e00-65ae-7092d936bcec"
            }

        response = requests.delete(url, headers=headers)

        print("delete dashboard", response.status_code, response.text, response.cookies)


    # b = requests.get("https://vebd1.vertexinc.com/vertex/open-ws/veit/vebd/hivetables/getTablesByDB?databaseName=vedemo", auth =('vedemo', 'iL0veTax'))
    #
    # url = "https://vebd1.vertexinc.com/vertex/open-ws/veit/vebd/veuserses/login"
    #
    # payload = "{}"
    # headers = {
    #     'authorization': "Basic dmVkZW1vOmlMMHZlVGF4",
    #     'origin': "https://vebd1.vertexinc.com",
    #     'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    #     'content-type': "application/json;charset=UTF-8",
    #     'accept': "*/*",
    #     'referer': "https://vebd1.vertexinc.com/vertex/open/veit/index.html",
    #     'accept-encoding': "gzip, deflate, br",
    #     'accept-language': "en-US,en;q=0.9",
    #     'cookie': "JSESSIONID=1tr0znfmc913hnxycbmssadal; _ga=GA1.2.819411697.1495725341; betatester=yes; netuser=yhailu",
    #     'cache-control': "no-cache",
    #     'postman-token': "0dc868b7-809d-ca72-f983-b562bbc3b202"
    # }
    #
    # a = requests.post(url, data=payload, headers=headers)
    # dash = requests.get('https://vebd1.vertexinc.com/vertex/open-ws/veit/vebd/querys/executeChartData/59fb8371e4b0ce82188a4eeb', auth =('vedemo', 'iL0veTax'))


    # create()
    getDashboards()
    # remove()
    # print("status: ", a.status_code)
    # print("status:", b.status_code)
    # print('status of dashboards: ', dash.status_code)


