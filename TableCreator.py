import time

from robot.api import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from BaseClasses.Locators import locators
from BaseClasses.singleton import Driver


class Tables(Driver):

    def __init__(self, driver):
        self.driver = driver


    def error_msg(self):
        """Method will return True an error message is displayed in the UI
           Otherwise this method will return False, If False is returned we assume
           that there is no error on the screen. Will have to write similar service for REST api testing
           to see what code you get back form service"""
        try:
            assert '<div class="alert alert-danger hidden">' in self.driver.page_source
        except AssertionError:
            logger.error("Something went wrong. Check issue.")
            logger.info("Something went wrong.")
            logger.debug("Something went wrong")
            return True

        return False

    def create_table(self, db_name, table_name, col_names, table_num):
        """If this keyword does not throw an error in console, we can assume that the test has passed"""

        tableLink = self.driver.find_element(locators['table.creator.button'][0],
                                             locators['table.creator.button'][1])
        tableLink.click()
        time.sleep(1)

        # if self.error_msg():
        #     logger.console("Something went wrong")
        #     self.close_driver_broswer()


        xPathToDBName ="//*[@id='tool-content']/div/div/fieldset[1]/div/section[1]/select/option[@label='{}']".format(db_name)

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "tool-content"))
            )
        except:
            logger.console("Element not found!")
            self.driver.quit()

        selectDB = self.driver.find_element(By.XPATH, xPathToDBName)

        selectDB.click()

        tableName = self.driver.find_element(locators['table.name'][0], locators['table.name'][1])
        tableName.clear()
        tableName.send_keys(table_name)

        if table_num == 4:
            nonDel = self.driver.find_element(locators['table.4.del.none'][0], locators['table.4.del.none'][1])
            nonDel.click()

            optionQuote = self.driver.find_element(locators['table.4.quote'][0], locators['table.4.quote'][1])
            optionQuote.click()

            optionEscape = self.driver.find_element(locators['table.4.escape'][0], locators['table.4.escape'][1])
            optionEscape.click()

            optionSnakeCase = self.driver.find_element(locators['table.4.snake'][0], locators['table.4.snake'][0])
            optionSnakeCase.click()
        if table_num == 5:
            delPipe = self.driver.find_element(locators['table.5.del.pipe'][0], locators['table.5.del.pipe'][1])
            delPipe.click()

        tableCols = self.driver.find_element(locators['table.cols'][0], locators['table.cols'][1])
        tableCols.clear()
        tableCols.send_keys(col_names)
        tableCommize = self.driver.find_element(locators['table.commaize'][0], locators['table.commaize'][1])
        tableCommize.click()

        if table_num == 6:
            tableCols.send_keys(Keys.PAGE_DOWN)
            time.sleep(3)

        tableCreateButton = self.driver.find_element(locators['create.table.button'][0],
                                                     locators['create.table.button'][1])
        tableCreateButton.click()

        time.sleep(2)
        # try:
        #     myElem = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, 'id("content")/div[2]/article[1]/div[1]')))
        #     e = self.driver.find_element(By.XPATH, 'id("content")/div[2]/article[1]/div[1]')
        #     info = str(e.text)
        #     logger.console('msg: '+'{}'.format(info))
        # except:
        #     logger.error('ERROR')

        # if self.error_msg():
        #     logger.console("ERROR!")
        #     self.close_driver_broswer()

        # try:
        #     assert not '<div class="alert alert-success">' in self.driver.page_source
        # except AssertionError:
        #     logger.console("Success!")

        time.sleep(1)

    def delete_table(self, db_name, table_name):
        "Takes params: db and a table name and deletes the table"
        # dash = self.driver.find_element(locators['home.dashboard'][0], locators['home.dashboard'][1])
        # dash.click()
        # tableLink = self.driver.find_element(locators['table.creator.button'][0],
        #                                      locators['table.creator.button'][1])
        # tableLink.click()
        # time.sleep(3)
        # # tableLink.click()

        # d = self.driver.find_elements_by_xpath('//nav/ul/li/ul')
        # for c in d:
        #     if (c.text == "Saved Tables"):
        #         c.click()
        time.sleep(2)
        self.locate_table(db_name, table_name)

        deleteTableButton = self.driver.find_element(locators['table.delete.button'][0], locators['table.delete.button'][1])
        deleteTableButton.click()
        time.sleep(1)

        confirmDelete  = self.driver.find_element(locators['table.confirm.delete'][0], locators['table.confirm.delete'][1])
        confirmDelete.click()
        time.sleep(2)





    def add_col_to_table(self, db_name, table_name, col_name):
        "self explanatory method simpley adds col to a desired table"
        # dash = self.driver.find_element(locators['home.dashboard'][0], locators['home.dashboard'][1])
        # dash.click()
        # time.sleep(2)
        # tableLink = self.driver.find_element(locators['table.creator.button'][0],
        # locators['table.creator.button'][1])
        # tableLink.click()
        #
        # savedTables = self.driver.find_element(locators['savedTables'][0], locators['savedTables'][1])
        # savedTables.click()
        table = self.driver.find_element_by_xpath("//select/option[text() = '{}']".format(db_name))
        table.click()

        self.driver.find_element_by_xpath('id("columnListTbl")/thead[1]/tr[1]/th[1]/div[1]/input[1]').send_keys(table_name)
        self.driver.find_element_by_xpath('id("columnListTbl")/tbody[1]/tr[1]/td[9]/button[1]').click()
        time.sleep(2)

        colName = self.driver.find_element(locators['table.col.name'][0], locators['table.col.name'][1])
        colName.clear()
        if colName == None:
            colName.clear()
        else:
            colName.send_keys(col_name)
        time.sleep(2)

        addColToTable = self.driver.find_element(locators['add.col.to.table'][0], locators['add.col.to.table'][1])
        addColToTable.click()
        if self.error_msg():
            logger.error("ERROR: Maybe expected")
        time.sleep(2)



    def locate_table(self, db_name, table_name):
        """Utility to make our lives easier. This method is used a lot during
        our automation to locate desired DB and choose desire table"""
        time.sleep(1)

        # xPathToDBName = "/html/body/div[1]/div[2]/div/section/div/article/div/div/div/div/fieldset/div[1]/section/select" % db_name

        # tableToDelete = self.driver.find_element(By.CLASS_NAME, 'select').click()
        tableToDelete = self.driver.find_element_by_xpath("//select/option[text() = '{}']".format(db_name))
        print(str(tableToDelete))
        tableToDelete.click()
        time.sleep(1)

        tableToDelete = self.driver.find_element(locators['table.to.delete.name'][0],
                                                 locators['table.to.delete.name'][1])
        tableToDelete.clear()
        tableToDelete.send_keys(table_name)
        time.sleep(2)

    def close_driver_broswer(self):
        """Summary :
        closes selenium webdriver and chrome broswer automatically
        """
        self.driver.close()
        self.driver.quit()

