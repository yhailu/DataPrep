from Regression.AdHocQueries import AdHocQueries
from Regression.JoinsRegression import Joins
from Regression.ManualFileUpload import ManualFileUpload
from Regression.Mappings import Mappings
from Regression.RestAPI import RestAPI
from Regression.TableCreator import Tables
from Regression.UnionsRegression import Unions


class tableKeywords():
    '''our robot framework keywords for table regression automation'''
    a = Tables()

    def setup_test(self, url):
        self.a.setUpTest(url)
    def launch_url(self, url):
        self.a.launch_ve(url)
    def login_with_parameters(self, username, password):
        self.a.login_with_parameters(username, password)
    def create_table(self, tablename, colnames, tablenum):
        self.a.create_table(tablename, colnames, tablenum)
    def delete_table(self, db_name, table_name):
        self.a.delete_table(db_name, table_name)
    def add_column_to_table(self, db_name, table_name, col_name):
        self.a.add_col_to_table(db_name, table_name, col_name)
    def close_driver_broswer(self):
        self.a.close_driver_broswer()

class adhoc():
    """Adhoc query keywords"""
    # ROBOT_LIBRARY_SCOPE ='TEST SUITE'
    a = AdHocQueries()

    def setup_test(self):
        self.a.setUPTest()
    def launch_URL(self, url):
        self.a.launch_ve(url)
    def login(self, username, password):
        self.a.login(username, password)
    def select_db_table(self, db, table):
        self.a.select_db_table(db, table)
    def run_query(self):
        self.a.runQuery()
    def save_query(self, query_name):
        self.a.saveQuery(query_name)
    def add_col(self, optional_alias):
        self.a.addCol(optional_alias)
    def delete(self, name):
        self.a.delete_query(name)
    def close_test(self):
        self.a.close_driver_broswer()

class Mappings():
    a = Mapping()
    def setup_test(self):
        self.a.setUPTest()
    def launch_URL(self, url):
        self.a.launch_ve(url)
    def login(self, username, password):
        self.a.login(username, password)
    def select_db_table(self, source_db, source_table, dest_db, dest_table):
        self.a.select_db_table(source_db, source_table, dest_db, dest_table)
    def mapping_test(self):
        self.a.mapping_test()
    def delete_mapping(self, name):
        self.a.delete_mapping(name)
    def close_test(self):
        self.a.close_driver_broswer()

class Joins():
    a  = Joins()
    def setup_test(self):
        self.a.setUPTest()
    def launch_URL(self, url):
        self.a.launch_ve(url)
    def login(self, username, password):
        self.a.login(username, password)
    def select_dbs_tables(self, target_db, joins_db_a, joins_db_b, joins_table_a, joins_table_b):
        self.a.select_dbs_tables(target_db, joins_db_a, joins_db_b, joins_table_a, joins_table_b)
    def close_test(self):
        self.a.close_driver_broswer()

class Unions():
    a  = Unions()
    def setup_test(self):
        self.a.setUPTest()
    def launch_URL(self, url):
        self.a.launch_ve(url)
    def login(self, username, password):
        self.a.login(username, password)
    def union(self):
        self.a.union()
    def close_test(self):
        self.a.close_driver_broswer()

class manualFileUpload():
    """keywords for manual file upload"""
    ROBOT_LIBRARY_SCOPE ='TEST SUITE'
    a = ManualFileUpload()

    def setup_test(self):
        self.a.setUPTest()
    def launch_URL(self, url):
        self.a.launch_ve(url)
    def login_with_parameters(self, username, password):
        self.a.login(username, password)
    def manual_file_upload(self, dir):
        self.a.manualFileUpload(dir)
    def close_driver_browser(self):
        self.a.close_driver_browser()

class RestAPI():
    """Keywords to implement our REST API framework for our automation"""# from Regression.MappingRegession import Mapping

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    rest_client = RestAPI()
    def get(self, url):
        self.rest_client._get_request(url)
    def post(self, url):
        self.rest_client._post_request(url)
    def delete(self, url, name):
        self.rest_client._delete_request(url, name)






