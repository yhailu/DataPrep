import time

import pyautogui
from robot.api import logger

from BaseClasses.Locators import locators
from BaseClasses.singleton import Driver
from Regression.AdHocQueries import AdHocQueries
from Regression.JoinsRegression import Joins
from Regression.ManualFileUpload import ManualFileUpload
from Regression.Mappings import Mappings
from Regression.TableCreator import Tables
from Regression.UnionsRegression import Unions


class testRunner(Driver):
    def __init__(self):
        Driver.__init__(self)
        self.driver = self.driver()

    def getDriver(self):
        return self.driver

    def login(self, username, password):
        userName = self.driver.find_element(locators['login.username'][0], locators['login.username'][1])
        userName.send_keys(username)

        passWord = self.driver.find_element(locators['login.password'][0], locators['login.password'][1])
        passWord.send_keys(password)
        signInButton = self.driver.find_element(locators['login.signin.button'][0], locators['login.signin.button'][1])
        signInButton.click()

    def launch_ve(self, url):
        """Launch our application with url being passed as a parameter string"""
        self.driver.get(url)
        self.driver.maximize_window()

    def menu_option(self, option):
        e = self.driver.find_elements_by_xpath('//nav/ul/li')
        for a in e:
            if (a.text == option):
                a.click()

    def sub_menu(self, option):
        d = self.driver.find_elements_by_xpath('//nav/ul/li/ul')
        for c in d:
            if (c.text == option):
                c.click()

    def logout(self):
        self.driver.find_element_by_xpath('id("header")/div[2]/div[6]/span[1]/a[1]').click()
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')

    def close_driver_broswer(self):
        self.driver.close()
        self.driver.quit()


    def error(self):
        error = ' '
        try:
            assert '<div class="alert alert-danger hidden"' in self.driver.page_source
        except AssertionError:
             logger.error('Error')
             errors = self.driver.find_elements_by_xpath('id("content")/div/article/div')
             for error in errors:
                 logger.console(error.text)


class regressionKeywords():
    testRunner = testRunner()
    driver = testRunner.getDriver()

    tblTest = Tables(driver)
    fileUpload = ManualFileUpload(driver)
    adhocTest = AdHocQueries(driver)
    mappingsTest = Mappings(driver)
    unionsTest = Unions(driver)
    joinsTest = Joins(driver)



    def launch_test(self, url, uname, pwd):
        self.testRunner.launch_ve(url)
        self.testRunner.login(uname, pwd)

    def logout(self):
        self.testRunner.logout()

    """TABLES"""
    def create_table(self, db_name, tablename, colnames, tablenum):
        self.tblTest.create_table(db_name, tablename, colnames, tablenum)
        self.testRunner.error()
        time.sleep(2)

    def delete_table(self, db_name, table_name):
        self.testRunner.menu_option('Table Creator')
        self.testRunner.sub_menu('Saved Tables')
        time.sleep(2)
        self.tblTest.delete_table(db_name, table_name)
        self.testRunner.error()

    def add_col_to_table(self, db_name, table_name, col_name):
        self.testRunner.menu_option('About VE')
        self.testRunner.menu_option('Table Creator')
        self.testRunner.sub_menu('Saved Tables')
        self.tblTest.add_col_to_table(db_name, table_name, col_name)
        self.testRunner.error()

    """MANUAL FILE UPLOAD"""
    def manual_file_upload(self, dir):
        self.fileUpload.manualFileUpload(dir)

    """ADHOC"""
    def select_db_table(self, db, table):
        self.testRunner.menu_option('Adhoc Queries')
        self.adhocTest.select_db_table(db, table)
        self.testRunner.error()

    def adhoc_filter(self, option, filter_val):
        self.adhocTest.filter(option, filter_val)
        self.testRunner.error()

    def run_query(self):
        self.adhocTest.runQuery()
        self.testRunner.error()

    def save_query(self, query_name, query_desc, save_as_new_query):
        self.adhocTest.saveQuery(query_name, query_desc, save_as_new_query)
        self.testRunner.error()

    def add_col(self, optional_alias):
        self.adhocTest.addCol(optional_alias)
        self.testRunner.error()

    def delete_query(self, name):
        self.testRunner.menu_option('Adhoc Queries')
        self.adhocTest.delete_query(name)
        self.testRunner.error()

    def pivot_test(self, db, table):
        # self.testRunner.menu_option('Adhoc Queries')
        time.sleep(3)
        self.adhocTest.select_db_table(db, table)
        self.adhocTest.pivot_test()

    """Joins"""
    def joins_select_dbs_tables(self, target_db, joins_db_a, joins_db_b, joins_table_a, joins_table_b):
        self.testRunner.menu_option('Joins')

    def joins_regression(self):
        self.testRunner.menu_option('Joins')
        self.joinsTest.joins_regression()

    """Unions"""
    def union(self):
        self.testRunner.menu_option('Unions')
        self.unionsTest.union()

    def delete_union(self, union):
        self.unionsTest.delete_union(union)

    def open_and_run(self, union):
        self.unionsTest.open_and_run(union)

    def unions_regression(self):
        self.testRunner.menu_option('Unions')
        self.unionsTest.unions_regression()

    """MAPPINGS"""
    def mappings_select_db_table(self, source_db, source_table, dest_db, dest_table):
        self.testRunner.menu_option('Mapping')
        self.mappingsTest.select_db_table(source_db, source_table, dest_db, dest_table)

    def map_source_to_dest(self, source, destination):
        self.mappingsTest.map_source_to_dest(source, destination)

    def save_mappings(self, map_name, map_desc):
        self.mappingsTest.sample_all_rows()
        self.mappingsTest.save_mapping(map_name, map_desc)

    def mapping_test(self):
        self.mappingsTest.mapping_test()
        time.sleep(5)
    def run_mapping(self):
        self.mappingsTest.run_mapping()
    def delete_mapping(self, name):
        self.testRunner.menu_option('Mapping')

        time.sleep(2)
        self.mappingsTest.delete_mapping(name)

    def map_test(self):
        self.mappingsTest.run_map_with_exisiting_name()
        self.mappingsTest.edit_an_existing_map()
        self.mappingsTest.run_map_from_save_screen()

    """CLOSE DRIVER AND BROWSER"""
    def close_test(self):
        self.testRunner.close_driver_broswer()




