import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from robot.api import logger
from BaseClasses.Locators import locators
from BaseClasses.singleton import Driver
from BaseClasses.singleton import highlight
import pyautogui


# from BaseClasses.UI import UI

class AdHocQueries(Driver):
    """Adhoc Queries Keywords"""
    def __init__(self, driver):
        self.driver = driver

    def select_db_table(self, db_name, table_name):
        """

        Args:
            db_name: name of database to be selected
            table_name: name of table to be selected

        Returns: void

        """

        """Utiltity that lets us choose a database and table name from dropdown"""


        xPathToDBName = "//*[@id='select-database']/select/option[text()='%s']" % db_name

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "select-database"))
            )
        except:
            logger.console("Element not found!")
            self.driver.quit()

        selectDB = self.driver.find_element(By.XPATH, xPathToDBName)
        # highlight(selectDB)
        selectDB.click()



        xPathToTable = "//*[@id='select-table']/select/option[text()='%s']" % table_name
        selectTable = self.driver.find_element(By.XPATH, xPathToTable)
        selectTable.click()
        time.sleep(5)

    def runQuery(self):
        """

        Summary: hits run query button

        Returns: None

        """
        runAdhocQuery = self.driver.find_element(locators['adhoc.runAdhocQuery'][0], locators['adhoc.runAdhocQuery'][1])
        runAdhocQuery.click()

    def saveQuery(self, query_name, query_desc, save_as_new_query):
        """
        Summary: Save a query

        Args:
            query_name: Name of query to be saved as String

        Returns: void

        """
        saveThisQuery = self.driver.find_element(locators['adhoc.saveThisQuery'][0], locators['adhoc.saveThisQuery'][1])
        saveThisQuery.click()
        time.sleep(2)
        if save_as_new_query == 'True':
            time.sleep(3)
            driver = self.driver
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div[2]/div[1]/section[1]/div/label[2]/i").click()  # Save As
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div[2]/div[1]/section[2]/label/input").click()  # Viewable by team
            driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div[2]/div[2]/section[3]/label[2]/input").click()  # Save as table
            driver.find_element_by_name("mapname").clear()
            driver.find_element_by_name("mapname").send_keys("AutoQuery2")
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
            time.sleep(3)
            self.wait_for_success()
            time.sleep(3)

            driver.find_element_by_css_selector("button.btn.btn-primary.pull-right").click()
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").clear()
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
            driver.find_element_by_xpath(
                "//*[@id='columnListTbl']/tbody/tr[4]/td[5]/select/option[text()='sum']").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[5]/td[1]/input").click()
            driver.find_element_by_xpath(
                "//*[@id='columnListTbl']/tbody/tr[5]/td[5]/select/option[text()='avg']").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[6]/td[1]/input").click()
            driver.find_element_by_xpath(
                "//*[@id='columnListTbl']/tbody/tr[6]/td[5]/select/option[text()='count']").click()
            time.sleep(1)
            driver.find_elements_by_xpath("//html//div[@class='row']//tr[4]/td[7]")
            driver.find_element_by_id("runAdhocQuery").click()
            time.sleep(3)
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
            return

        queryName = self.driver.find_element(locators['query.name'][0], locators['query.name'][1])
        queryName.send_keys(query_name)
        self.driver.find_element_by_name("mapdesc").send_keys(query_desc)

        querySaveButton = self.driver.find_element(locators['query.save.button'][0], locators['query.save.button'][1])
        highlight(querySaveButton)
        querySaveButton.click()
        time.sleep(3)
        self.wait_for_success()

    def filter(self, option, filter_val):
        """

        Summary: component to deal with filter in adhoc screen

        Args:
            option: name of filter from dropdown
            filter_val: string to pass into filter field

        Returns:

        """
        filter = "//*[@id='columnListTbl']/tbody/tr[2]/td[6]/select/option[@value='{}']".format(option)
        click_filter = self.driver.find_element_by_xpath(filter)
        click_filter.click()
        if option == 'in':
            self.driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[2]/td[7]/div/button").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/input").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/input").click()
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
            time.sleep(2)
            self.runQuery()
            time.sleep(2)
            return

        if option =='not in':
            self.driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr[2]/td[7]/div/button").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[1]/input").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/input").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/input").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[1]/input").click()
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
            time.sleep(2)
            self.runQuery()
            time.sleep(2)
            return
        self.driver.find_element_by_xpath(
            "//*[@id='columnListTbl']/tbody/tr[2]/td[7]/div/span/input").clear()
        self.driver.find_element_by_xpath(
            "//*[@id='columnListTbl']/tbody/tr[2]/td[7]/div/span/input").send_keys(filter_val)
        time.sleep(1)
        self.runQuery()

    def pivot_test(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='select-database']/p/span[1]").click()
        driver.find_element_by_id("runAdhocQuery").click()
        driver.find_element_by_xpath('id("queryForm")/fieldset[1]/ul[1]/li[4]/a[1]').click()

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

    def addCol(self, optional_alias):
        """

        Args:
            optional_alias: name of option alias as string

        Returns: void

        """
        """

        TODO: thinking about making a command class/method that will handle constructing commands for us

        """
        offset = 1
        col = 'filename'
        len = 4
        command = 'substr(%s, %s, %s)' % (col, offset, len)

        time.sleep(5)
        addColButton  = self.driver.find_element(locators['query.add.col'][0], locators['query.add.col'][1])
        highlight(addColButton)
        addColButton.click()

        enterCommand = self.driver.find_element(locators['query.command'][0], locators['query.command'][1])
        highlight(enterCommand)
        enterCommand.send_keys(command)

        optionalAlias = self.driver.find_element(locators['query.optional.alias'][0], locators['query.optional.alias'][1])
        # highlight(optionalAlias)
        optionalAlias.send_keys(optional_alias)
        time.sleep(2)



    def wait_for_success(self):
        try:
            myElem = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, 'id("content")/div[2]/article[1]/div[1]')))
            e = self.driver.find_element(By.XPATH, 'id("content")/div[2]/article[1]/div[1]')
            info = str(e.text)
            logger.console('{}'.format(info), newline=False)
        except:
            logger.error('ERROR')

    def delete_query(self, name):
        """

        Summary: Delete's a query

        Args:
            name: Name of Query we want to delete

        Returns: void

        """
        time.sleep(2)
        savedQueries = self.driver.find_element(locators['saved.queries'][0], locators['saved.queries'][1])
        savedQueries.click()
        time.sleep(3)

        filterName = self.driver.find_element(locators['queries.filter.name'][0], locators['queries.filter.name'][1])
        filterName.clear()
        filterName.send_keys(name)

        deleteQuery = self.driver.find_element(locators['delete.query'][0], locators['delete.query'][1])
        deleteQuery.click()
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)

        try:
            myElem = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, 'id("content")/div[2]/article[1]/div[1]')))
            e = self.driver.find_element(By.XPATH, 'id("content")/div[2]/article[1]/div[1]')
            info = str(e.text)
            logger.console('{}'.format(info), newline=False)
        except:
            logger.error('ERROR')





    def close_driver_broswer(self):

        """

        Summary: Close open browser and selenium driver will be closed as a
                 process so no need to do this manually

        """

        self.driver.close()
        self.driver.quit()





