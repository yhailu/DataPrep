import time
import pickle
from robot.api import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from BaseClasses.Locators import locators
from BaseClasses.singleton import Driver
from BaseClasses.singleton import highlight
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class test(Driver):
    def __init__(self):
        Driver.__init__(self)
        self.driver = self.driver()
        self.driver.get('https://vebd2.vertexinc.com/vertex/sanity-sso/auth/login.html?originalUrl=https://vebd2.vertexinc.com/vertex/sanity/ve/#/login')
        self.driver.maximize_window()
        userName = self.driver.find_element(locators['login.username'][0], locators['login.username'][1])
        userName.send_keys('sri')

        passWord = self.driver.find_element(locators['login.password'][0], locators['login.password'][1])
        passWord.send_keys('iL0veTax')

        signInButton = self.driver.find_element(locators['login.signin.button'][0], locators['login.signin.button'][1])
        signInButton.click()
        signInButton.click()

        adhocButton = self.driver.find_element(locators['adhoc.button'][0], locators['adhoc.button'][1])
        highlight(adhocButton)
        adhocButton.click()
        xPathToDBName = "//*[@id='select-database']/select/option[text()='%s']" % 'open_yesu_test'

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "select-database"))
            )
        finally:
            logger.console("Element not found!")
            self.driver.quit()

        selectDB = self.driver.find_element(By.XPATH, xPathToDBName)
        highlight(selectDB)
        selectDB.click()

        xPathToTable = "//*[@id='select-table']/select/option[text()='%s']" % 'open_dan'
        selectTable = self.driver.find_element(By.XPATH, xPathToTable)
        selectTable.click()
        time.sleep(5)

        runAdhocQuery = self.driver.find_element(locators['adhoc.runAdhocQuery'][0], locators['adhoc.runAdhocQuery'][1])
        highlight(runAdhocQuery)
        runAdhocQuery.click()

        inputs = self.driver.find_elements_by_xpath('body.desktop-detected.ng-scope:nth-child(2) div.ng-scope:nth-child(1) div.ng-scope:nth-child(2) div.animated.fadeIn.ng-scope section.ng-scope:nth-child(5) div.row:nth-child(1) article.col-xs-12.col-sm-12.col-md-12.col-lg-12.sortable-grid.ui-sortable div.jarviswidget.jarviswidget-sortable div.widget-body.no-padding div.smart-form.ng-valid.ng-valid-pattern.ng-valid-maxlength.ng-dirty.ng-valid-parse div.row:nth-child(3) section.col.col-12 div.fixed-table-container table.table.table-bordered.table-striped tbody.ng-scope:nth-child(2) tr.vs-repeat-repeated-element.ng-scope:nth-child(4) > td:nth-child(7)')

        for input in inputs:
            print(inputs.text)
    def cookies(self):
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print(str(cookie))
class testMaps(Driver):
    def __init__(self):
        Driver.__init__(self)
        self.driver = self.driver()
        self.driver.get("https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login")
        self.driver.maximize_window()
        self.driver.find_element_by_name("username").send_keys("daniel")
        self.driver.find_element_by_name("password").send_keys("iL0veTax")
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()

        # Open Maps Tab
        self.driver.find_element_by_xpath("//*[text()='Mapping']").click()

        # Select DBs and Tables
        self.wait_by_name('sourceDB')
        self.driver.find_element_by_xpath("//select[@name='sourceDB']/option[text()='open_dan']").click()
        self.driver.find_element_by_xpath("//select[@name='destDB']/option[text()='open_dan']").click()
        self.driver.find_element_by_xpath("//select[@name='sourceTable']/option[text()='autotable1']").click()
        self.driver.find_element_by_xpath("//select[@name='destTable']/option[text()='autotable2']").click()




        jquery_url = 'http://code.jquery.com/jquery-1.11.2.min.js'




        self.driver.set_script_timeout(30)
        # self.map_source_to_dest('filename', 'big3')
        # self.map_source_to_dest('int2', 'big3')

        # self.driver.find_element_by_xpath('id("wid-id-0")/div[1]/div[2]/div[1]/fieldset[1]/div[2]/div[1]/div[1]/div[3]/div[1]/a[1]').click()
        #
        # common_funcs = self.driver.find_elements_by_xpath('id("wid-id-0")/div/div/div/fieldset/div[2]/div/div/div/div/ul')
        # for a in common_funcs:
        #     print(a.text)

        # """Source fields to destination fields map Example"""
        # self.map_source_to_dest('double4', 'int2')
        #
        # "Example 2"
        # self.map_source_to_dest('big3', 'big3')
        #
        # "Insert Functions to Destination fiels map Example "
        # self.functions_to_destination_table('Commonly Used Functions', 'lookup', 'double4')
        #
        # self.functions_to_destination_table('Vertex Functions','currXRate', 'string1')
        # self.functions_to_nest_function('Commonly Used Functions', 'lookup', 'From Currency')
        # self.functions_to_nest_function('Commonly Used Functions', 'toDouble', 'Date')

        #id("udmcolumnListTbl")/tbody[1]/tr[2]/td[1]/ul[1]/li[1]/div[2]/div[1]/ul[1]/li[2]/div[2]/ul[1]
        #id("udmcolumnListTbl")/tbody[1]/tr[2]/td[1]/ul[1]/li[1]/div[2]/div[1]/ul[1]/li[1]/div[2]/ul[1]/li[1]/div[2]/div[1]/ul[1]/li[1]/div[2]/ul[1]
        #id("udmcolumnListTbl")/tbody[1]/tr[2]/td[1]/ul[1]/li[1]/div[2]/div[1]/ul[1]/li[1]/div[2]/ul[1]/li[1]/div[2]/div[1]/ul[1]/li[2]/div[2]/ul[1]
        self.map_source_to_dest('string1', 'big3')



        self.driver.close()
        self.driver.quit()

    def load_js(self):
        """

        Returns: drag and drop js for selenium to execute

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
        try:
            myElem = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.NAME, elem)))
            print
            "Page is ready!"
        except:
            print ("Loading took too much time!")
class adhoc(Driver):
    def __init__(self):
        Driver.__init__(self)
        self.driver = self.driver()


        driver = self.driver
        driver.get("https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login")
        driver.maximize_window()
        driver.find_element_by_name("username").send_keys("daniel")
        driver.find_element_by_name("password").send_keys("iL0veTax")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(3)

        # Open Adhoc screen
        driver.find_element_by_xpath("//*[text()='Adhoc Queries']").click()
        time.sleep(3)

        # Select DB and Table
        driver.find_element_by_xpath("//*[@id='select-database']/select/option[text()='open_automated']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='select-table']/select/option[text()='autotable1']").click()
        time.sleep(3)

        # Run Query
        driver.find_element_by_id("runAdhocQuery").click()
        time.sleep(2)

        # Save Query
        driver.find_element_by_xpath("//*[@id='queryForm']/fieldset/div[3]/section/div[2]/div/button[1]").click()
        driver.find_element_by_name("mapname").send_keys("AutoQuery1")
        driver.find_element_by_name("mapdesc").send_keys("AutoQuery Description")
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\Automation\\Screenshots\\Regression\\AdhocSuccessSave.png")
        time.sleep(5)

        # Save As New Query
        driver.find_element_by_xpath("//*[@id='select-table']/select/option[text()='autotable2']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='select-database']/p/span[1]").click()
        driver.find_element_by_id("runAdhocQuery").click()
        time.sleep(3)
        # driver.find_element_by_xpath("//*[@id='ve_dt_basic_filter']/label/input").send_keys(Keys.PAGE_UP)
        # time.sleep(3)
        driver.find_element_by_css_selector("button.btn.btn-info.btn-sm").click()
        # driver.find_element_by_xpath("[@id='queryForm']/fieldset/div[3]/section/div[2]/div/div/button[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div[2]/div[1]/section[1]/div/label[2]/i").click()  # Save As
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div[2]/div[1]/section[2]/label/input").click()  # Viewable by team
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div[2]/div[2]/section[3]/label[2]/input").click()  # Save as table
        driver.find_element_by_name("mapname").clear()
        driver.find_element_by_name("mapname").send_keys("AutoQuery2")
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(8)

        ##Edit Saved Query.  Add Column, with function, Sum/Avg/Count##
        # driver.find_element_by_xpath("[@id='queryForm']/fieldset/div[3]/section/div[2]/div/div/button[2]").click()
        driver.find_element_by_css_selector("button.btn.btn-primary.pull-right").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys("autoquery1")
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[1]/td[8]/button[1]").click()
        time.sleep(7)
        # Add Column
        # driver.find_element_by_xpath("//*[@id='queryForm']/fieldset/div[1]/div[1]/button").click()
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[2]/td[2]/input").send_keys(
            "substr(string1,1,4)")
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[2]/td[4]/input").send_keys("SubstringTest")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[4]/td[1]/input").click()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[4]/td[5]/select/option[text()='sum']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[5]/td[1]/input").click()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[5]/td[5]/select/option[text()='avg']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[6]/td[1]/input").click()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[6]/td[5]/select/option[text()='count']").click()
        time.sleep(1)
        driver.find_element_by_id("runAdhocQuery").click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\Automation\\Screenshots\\Regression\\AdhocSumAvgCount.png")
        # Save Edited Query
        driver.find_element_by_css_selector("button.btn.btn-info.btn-sm").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div[2]/div[1]/section[1]/div/label[2]/i").click()  # Save As
        driver.find_element_by_name("mapname").clear()
        driver.find_element_by_name("mapname").send_keys("AutoQuery3")
        driver.find_element_by_name("mapdesc").clear()
        driver.find_element_by_name("mapdesc").send_keys("AutoQuery Description")
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(8)

        # Delete Query
        driver.find_element_by_xpath("//*[@id='queryForm']/fieldset/div[1]/section[3]/section/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys("autoquery2")
        driver.find_element_by_css_selector("button.btn.btn-default.pull-right.btn-xs").click()
        time.sleep(5)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)
        # driver.get_screenshot_as_file("C:\\Automation\\Screenshots\\Regression\\AdhocDelete.png")


        ###Pivot Test###
        # Open Queries Tab
        driver.find_element_by_xpath("//*[text()='Adhoc Queries']").click()
        time.sleep(3)

        # Select DB and Table
        driver.find_element_by_xpath("//*[@id='select-database']/select/option[text()='open_automated']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='select-table']/select/option[text()='autotable1']").click()
        time.sleep(3)

        # Run Query
        driver.find_element_by_xpath("//*[@id='select-database']/p/span[1]").click()
        driver.find_element_by_id("runAdhocQuery").click()

        # Select Pivot
        driver.find_element_by_xpath("//*[@id='content']/ul/li[4]/a").click()

        # Pivot table settings
        driver.find_element_by_xpath("//*[@id='s3']/div[2]/div[1]/section/select/option[text()='string1']").click()
        driver.find_element_by_xpath("//*[@id='s3']/div[1]/section[2]/div[1]/select/option[text()='int2']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='s3']/div[1]/section[2]/div[3]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div[2]/div/div[2]/table/thead/tr/th[1]/div/button[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(5)
        driver.find_element_by_id("runPivot").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='ve_dt_basic_length']/label/select/option[text()='All']").click()
class testJoins(Driver):
    def __init__(self):
        pass
    def menu_option(self, option):
            e = self.driver.find_elements_by_xpath('//nav/ul/li')
            for a in e:
                if (a.text == option):
                    a.click()

    def sub_menu(self, option):
            d = self.driver.find_elements_by_xpath('//nav/ul/li/ul')
            for c in d:
                c.click()
                if (c.text == option):
                    pass





if __name__ == "__main__":

        test()
