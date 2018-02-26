import time

import pyautogui
from selenium.webdriver.common.by import By

from BaseClasses.Locators import locators
from BaseClasses.singleton import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from robot.api import logger


class Mappings():
    def __init__(self, driver):
        self.driver = driver

    def run_mapping(self):
        """

        Returns: void

        """
        # mappingButton = self.driver.find_element(locators['mapping.button'][0], locators['mapping.button'][1])
        # mappingButton.click()
        driver = self.driver
        driver.find_element_by_css_selector(".btn.btn-default.ng-pristine.ng-valid.ng-scope").click()
        time.sleep(3)
        driver.find_element_by_name("columns").click()
        driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()
        time.sleep(15)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)

    def select_db_table(self, source_db, source_table, dest_db, dest_table):

        """

        Args:
            source_db: name of src db
            source_table: name of src table
            dest_db: name of destination db
            dest_table: name of destination table

        Returns: void

        """

        time.sleep(2)
        xPathToSourceDBName = "//select[@name='sourceDB']/option[text()='{}']".format(source_db)

        # try:
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, xPathToSourceDBName))
        #     )
        # except:
        #     logger.console("Element not found!")
        #     self.driver.quit()

        select_source_db = self.driver.find_element(By.XPATH, xPathToSourceDBName)
        # highlight(select_source_db)
        select_source_db.click()

        xPathToSourceTable = "//select[@name='sourceTable']/option[text()='{}']".format(source_table)
        selectSourceTable = self.driver.find_element(By.XPATH, xPathToSourceTable)
        selectSourceTable.click()

        xPathToDestDBName = "//select[@name='destDB']/option[text()='{}']".format(dest_db)
        select_dest_db = self.driver.find_element(By.XPATH, xPathToDestDBName)
        select_dest_db.click()

        xPathToDestTableName = "//select[@name='destTable']/option[text()='{}']".format(dest_table)
        select_dest_table = self.driver.find_element(By.XPATH, xPathToDestTableName)
        select_dest_table.click()

    def mapping_test(self):

        self.drag_and_drop(locators['map.string'][1], locators['map.strings'][1])
        self.drag_and_drop(locators['mapping.if'][1], locators['mapping.if.to'][1])
        self.drag_and_drop(locators['mapping.currxrate'][1], locators['mapping.currxrate.to'][1])


        mapname = self.driver.find_element(locators['mapname'][0], locators['mapname'][1])
        mapname.send_keys('autoMaptest1')

        mapdesc = self.driver.find_element(locators['mapping.desc'][0], locators['mapping.desc'][1])
        mapdesc.send_keys('test desc')

        saveButton = self.driver.find_element(locators['save.mapping.button'][0], locators['save.mapping.button'][1])
        saveButton.click()

    def sample_all_rows(self):
        self.driver.find_element(By.XPATH, 'id("btnGetTransform")')

    def save_mapping(self, map_name, map_desc):
        """
        Summary: if on mappings screen it will save a map for you

        Args:
            map_name: name our map anything we want
            map_desc: description of our map

        Returns: void

        """
        mapname = self.driver.find_element(locators['mapname'][0], locators['mapname'][1])
        mapname.send_keys(map_name)

        mapdesc = self.driver.find_element(locators['mapping.desc'][0], locators['mapping.desc'][1])
        mapdesc.send_keys(map_desc)

        saveButton = self.driver.find_element(locators['save.mapping.button'][0], locators['save.mapping.button'][1])
        saveButton.click()

    def drag_and_drop(self, f, t):
        """

        Args:
            f: from element to drag and drop
            t: drag and drop to

        Returns:

        """
        time.sleep(2)
        from_element = self.driver.find_element(By.XPATH, f)
        to_element = self.driver.find_element(By.XPATH, t)
        self.driver.execute_script(self.load_js(), from_element, to_element)
        time.sleep(2)

    def delete_mapping(self, name):
        """

        Args:
            name: Name of map that we want to delete

        Returns:

        """
        self.driver.find_element(By.XPATH, locators['saved.mappings'][1]).click()
        time.sleep(2)

        self.driver.find_element(locators['saved.mappings.filter'][0], locators['saved.mappings.filter'][1]).send_keys(name)
        time.sleep(3)
        self.driver.find_element(locators['saved.mappings.delete'][0], locators['saved.mappings.delete'][1]).click()
        pyautogui.press('enter')
        time.sleep(4)
        self.wait_for_success()

    def wait_for_success(self):
        """

        Summary: Waits for success message in the UI

        """
        try:
            myElem = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, 'id("content")/div[2]/article[1]/div[1]')))
            e = self.driver.find_element(By.XPATH, 'id("content")/div[2]/article[1]/div[1]')
            info = str(e.text)
            logger.console('{}'.format(info), newline=False)
        except:
            logger.error('ERROR')

    def load_js(self):
        """

        Summary: load our drag and drop helper for us
        returns: js

        """
        with open("C:\\Users\\yhailu\\PycharmProjects\\DataPrep\\js\\dragdrop_helper.js") as f:
            js = f.read()
        return js

    def functions_to_nest_function(self, category, _function, field_in_function):
        """

        Args:
            category: 'Commonly Used Function' or 'Date/Time Functions' or 'General Function' or 'Vertex Functions'
            _function: function from one of the dropdowns clicked on when choosing category
            field_in_function: field in function in destination table that you want to nest

        Returns: None, executes js

        """

        """"For method to work the function that you want to nest, must have already been dragged into destionatin table
        e.g. self.functions_to_destination_table('Vertex Functions','currXRate', 'string1')"""""
        function_body = self.driver.find_elements(By.XPATH, 'id("udmcolumnListTbl")/tbody/tr/td/ul/li/div/div/ul/li/div')
        to = ''
        source = ''
        counter = 1  # xpath starts at 1, so we can adjust accordingly
        for a in function_body:
            # print('a.text' + a.text)
            if a.text == field_in_function:
                break
            if a.text == '':
                continue
            else:
                counter = counter + 1 #increment counter

        # print('Counter' + str(counter))
        path = 'id("udmcolumnListTbl")/tbody[1]/tr[2]/td[1]/ul[1]/li[1]/div[2]/div[1]/ul[1]/li[' + str(
            counter) + ']/div[2]/ul[1]'
        to = self.driver.find_element_by_xpath(path)
        self.driver.find_element(By.LINK_TEXT, category).click()
        common_functions = self.driver.find_elements_by_xpath(
            'id("wid-id-0")/div/div/div/fieldset/div[2]/div/div/div/div/ul/li/div')

        for a in common_functions:
            if a.text == _function:
                source = a
        # to = self.driver.find_element_by_xpath('id("udmcolumnListTbl")/tbody[1]/tr[2]/td[1]/ul[1]/li[1]/div[2]/div[1]/ul[1]/li[1]/div[2]/ul[1]')
        time.sleep(2)
        # highlight(source)
        self.driver.execute_script(self.load_js(), source, to)
        time.sleep(2)

    def functions_to_destination_table(self, category, function, destination):
        """

        Args:
            category: 'Commonly Used Function' or 'Date/Time Functions' or 'General Function' or 'Vertex Functions'
            function: From one of the selections from clicking on a category choose a function from the dropdown
            destination: Field name in destination table that you want

        Returns: Void, executes js

        """
        self.driver.find_element(By.LINK_TEXT, category).click()
        _functions = self.driver.find_elements_by_xpath(
            'id("wid-id-0")/div/div/div/fieldset/div[2]/div/div/div/div/ul/li/div')
        source = ' '

        for a in _functions:
            if a.text == function:
                source = a

        table1 = self.driver.find_elements_by_xpath('id("udmcolumnListTbl")/tbody/tr/td/div/div/span')

        """what row the destination table starts with in html tr[2] so counter = 2"""
        counter = 2

        for a in table1:
            if a.text == destination:
                break
            counter = counter + 1

        path = 'id("udmcolumnListTbl")/tbody[1]/tr[' + str(counter) + ']/td[1]/ul[1]'
        dest = self.driver.find_element_by_xpath(path)
        time.sleep(2)
        self.driver.execute_script(self.load_js(), source, dest)
        time.sleep(2)

    def map_source_to_dest(self, source, destination):
        """

        Args:
            source: name of field from source table
            destination: name of the field in destination table that you want to map to

        Returns: Void, executes js

        """
        """var to should be 'from' from a convention naming standpoint"""
        source_table = self.driver.find_elements_by_xpath('id("source-scroller")/div/div/div/span[1]')
        to = ''
        for a in source_table:
            if a.text == source:
                to = a

        table1 = self.driver.find_elements_by_xpath('id("udmcolumnListTbl")/tbody/tr/td/div/div/span')

        """what row the destination table starts with in html tr[2] so counter = 2"""
        counter = 2

        for a in table1:
            if a.text == destination:
                break
            counter = counter + 1

        path = 'id("udmcolumnListTbl")/tbody[1]/tr[' + str(counter) + ']/td[1]/ul[1]'
        dest = self.driver.find_element_by_xpath(path)
        time.sleep(1)
        self.driver.execute_script(self.load_js(), to, dest)
        time.sleep(1)

    def wait_by_name(self, elem):
        """

        Summary: will wait for element to come into view or else will throw an exception

        Args:
            elem: web driver element that we want to wait for

        Returns: void

        """
        try:
            myElem = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.NAME, elem)))
            print
            "Page is ready!"
        except:
            print ("Loading took too much time!")


    def run_map_from_save_screen(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/fieldset[1]/div[1]/section[4]/button").click()
        time.sleep(7)
        inputfield = driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input")
        inputfield.send_keys("AutomatedMap2")
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr/td[7]/div[1]/button[2]").click()
        time.sleep(3)
        driver.find_element_by_name("columns").click()
        driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()
        time.sleep(15)
        alert = driver.switch_to.alert
        alert.accept()
        inputfield.clear()

        time.sleep(5)

    def edit_an_existing_map(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/fieldset/div[1]/section[4]/button[1]").click()
        time.sleep(7)
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys("AutomatedMap1")
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr/td[7]/div[1]/button[1]").click()  # Edit Button
        time.sleep(5)
        driver.find_element_by_id("mapname").clear()
        driver.find_element_by_id("mapname").send_keys("AutomatedMap2")
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/footer/div/section/div/label[2]/input").click()
        driver.find_element_by_id("create-table").click()
        time.sleep(3)

    def run_map_with_exisiting_name(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='side-menu']/ul/li[10]/a/span").click()
        time.sleep(3)
        # Select DBs and Tables
        driver.find_element_by_xpath("//select[@name='sourceDB']/option[text()='open_automated']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//select[@name='destDB']/option[text()='open_automated']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//select[@name='sourceTable']/option[text()='autotable1']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//select[@name='destTable']/option[text()='autotable3']").click()
        time.sleep(3)
        # Automap
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/fieldset/div[2]/section/button").click()
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(3)
