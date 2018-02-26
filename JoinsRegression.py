import time

from robot.api import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from BaseClasses.Locators import locators
from BaseClasses.singleton import Driver
from selenium.webdriver.common.keys import Keys


class Joins():

    """
    Joins Keywords

    A lot of work needs to be done on this screen.
    """
    def __init__(self, driver):
        self.driver = driver

    def joins_regression(self):
        driver = self.driver
        ####Select Tables###
        # Set Target DB
        driver.find_element_by_xpath("//select[@name='sourceDB']/option[text()='open_automated']").click()
        time.sleep(3)

        # Set Table A DB
        driver.find_element_by_xpath(
            "//*[@id='join0']/div[2]/div[1]/div[1]/select/option[@label='open_automated']").click()
        time.sleep(3)

        # Set Table B DB
        driver.find_element_by_xpath(
            "//*[@id='join1']/div[2]/div[1]/div[1]/select/option[@label='open_automated']").click()
        time.sleep(3)

        # Select Table
        driver.find_element_by_xpath("//*[@id='join0']/div[2]/div[2]/div[3]/select/option[@label='autotable1']").click()
        driver.find_element_by_xpath("//*[@id='join1']/div[2]/div[2]/div[3]/select/option[@label='autotable2']").click()
        time.sleep(3)

        # Select Checkboxes
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[5]").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[8]").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[10]").click()
        time.sleep(3)

        # Input Field
        driver.find_element_by_xpath("//*[@id='join1']/div[2]/div[3]/table/tbody/tr[1]/td[3]/input").send_keys(
            "a.string1")

        # open Clause section
        driver.find_element_by_css_selector("button.btn.btn-default.btn-sm").click()

        # Setting 1st where clause
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[1]/input").send_keys(
            "a.string1")
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[2]/select/option[@value='=']").click()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[3]/span/input").send_keys(
            "string3")

        # Save Join
        driver.find_element_by_id("joinname").send_keys("AutoJoinClause")
        driver.find_element_by_name("mapdesc").send_keys("Testing where clause")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        time.sleep(3)

        # Run Join
        driver.find_element_by_xpath("//*[text()='Run Join']").click()
        time.sleep(3)
        driver.find_element_by_name("columns").click()
        driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()
        time.sleep(15)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)

        # Verify results in adhoc
        driver.find_element_by_xpath("//*[text()='Adhoc Queries']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='select-database']/select/option[text()='open_automated']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='select-table']/select/option[text()='autojoinclause']").click()
        time.sleep(3)

        # Run Query
        driver.find_element_by_id("runAdhocQuery").click()
        time.sleep(3)
        driver.get_screenshot_as_file(
            "C:\\Users\\dkrywko\\PycharmProjects\\Webinar\\Screenshots\\JoinWhereClauses\\JoinWhereEqual.png")

        # Testing Greater Than or Equal
        driver.find_element_by_xpath("//*[text()='Joins']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/fieldset[1]/div[1]/section[4]/button").click()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys("autojoinclause")
        driver.find_element_by_css_selector("button.btn.btn-primary.btn-xs").click()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[2]/select/option[@value='>=']").click()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[3]/span/input").clear()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[3]/span/input").send_keys(
            "string7")

        exec(open(
            "C:\\Users\\dkrywko\\PycharmProjects\\Webinar\\SeleniumScripts\\Joins\\JoinclauseRunAndAdhoc.py").read())
        # driver.get_screenshot_as_file("C:\\Users\\dkrywko\\PycharmProjects\\Webinar\\Screenshots\\JoinWhereClauses\\JoinWhereGreaterOrEqual.png")

        # Testing Greater Than
        driver.find_element_by_name("searchname").send_keys(Keys.PAGE_UP)
        driver.find_element_by_xpath("//*[text()='Joins']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/fieldset[1]/div[1]/section[4]/button").click()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys("autojoinclause")
        driver.find_element_by_css_selector("button.btn.btn-primary.btn-xs").click()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[2]/select/option[@value='>']").click()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[3]/span/input").clear()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[3]/span/input").send_keys(
            "string7")

        exec(open(
            "C:\\Users\\dkrywko\\PycharmProjects\\Webinar\\SeleniumScripts\\Joins\\JoinclauseRunAndAdhoc.py").read())
        # driver.get_screenshot_as_file("C:\\Users\\dkrywko\\PycharmProjects\\Webinar\\Screenshots\\JoinWhereClauses\\JoinWhereGreater.png")

        # Testing Less Than or Equal
        driver.find_element_by_name("searchname").send_keys(Keys.PAGE_UP)
        driver.find_element_by_xpath("//*[text()='Joins']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/fieldset[1]/div[1]/section[4]/button").click()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys("autojoinclause")
        driver.find_element_by_css_selector("button.btn.btn-primary.btn-xs").click()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[2]/select/option[@value='<=']").click()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[3]/span/input").clear()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[3]/span/input").send_keys(
            "string3")

        exec(open(
            "C:\\Users\\dkrywko\\PycharmProjects\\Webinar\\SeleniumScripts\\Joins\\JoinclauseRunAndAdhoc.py").read())
        # driver.get_screenshot_as_file("C:\\Users\\dkrywko\\PycharmProjects\\Webinar\\Screenshots\\JoinWhereClauses\\JoinWhereLessOrEqual.png")

        # Testing Less Than
        driver.find_element_by_name("searchname").send_keys(Keys.PAGE_UP)
        driver.find_element_by_xpath("//*[text()='Joins']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/fieldset[1]/div[1]/section[4]/button").click()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys("autojoinclause")
        driver.find_element_by_css_selector("button.btn.btn-primary.btn-xs").click()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[2]/select/option[@value='<']").click()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[3]/span/input").clear()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[3]/span/input").send_keys(
            "string3")

        exec(open(
            "C:\\Users\\dkrywko\\PycharmProjects\\Webinar\\SeleniumScripts\\Joins\\JoinclauseRunAndAdhoc.py").read())


    def select_dbs_tables(self, target_db, joins_db_a, joins_db_b, joins_table_a, joins_table_b):
        # self.driver.find_element(locators['joins.button'][0], locators['joins.button'][1]).click()
        xPathToTargetDB = "//select[@name='sourceDB']/option[text()='{}']".format(target_db)

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((locators['joins.button'][0], locators['joins.button'][1]))
            )
        except:
            logger.console("Element not found!")
            self.driver.quit()
        select_target_db = self.driver.find_element(By.XPATH, xPathToTargetDB)
        select_target_db.click()

        xPathToJoinsDBA = 'id("join0")/div[2]/div[1]/div[1]/select[1]/option[@label="{}"]'.format(joins_db_a)
        joins_DBA = self.driver.find_element(By.XPATH, xPathToJoinsDBA)
        joins_DBA.click()

        xPathToJoinsDBB = 'id("join1")/div[2]/div[1]/div[1]/select[1]/option[@label="{}"]'.format(joins_db_b)
        joins_DBB = self.driver.find_element(By.XPATH, xPathToJoinsDBB)
        joins_DBB.click()

        x_path_table_a = 'id("join0")/div[2]/div[2]/div[3]/select[1]/option[@label="{}"]'.format(joins_table_a)
        joins_a_table = self.driver.find_element(By.XPATH, x_path_table_a)
        joins_a_table.click()

        x_path_table_b = 'id("join1")/div[2]/div[2]/div[3]/select[1]/option[@label="{}"]'.format(joins_table_b)
        joins_b_table = self.driver.find_element(By.XPATH, x_path_table_b)
        joins_b_table.click()

        driver = self.driver
        # highlight(driver.find_element_by_xpath("//label[text()='a.string1']/preceding-sibling::input[@type='checkbox']"))

        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[5]").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[8]").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[10]").click()
        time.sleep(3)
        # Input Field
        driver.find_element_by_xpath("id('join1')/div[2]/div[3]/table[1]/tbody[1]/tr[1]/td[3]/input[1]").send_keys(
            "a.string1")

        # open Clause section
        driver.find_element_by_css_selector("button.btn.btn-default.btn-sm").click()

        # Setting 1st where clause
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[1]/input").send_keys(
            "a.string1")
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[2]/select/option[@value='=']").click()
        driver.find_element_by_xpath(
            "//*[@id='wid-id-0']/div/div[2]/div/fieldset[3]/div/section/div/div/section[3]/span/input").send_keys(
            "string3")

        # Save Join
        driver.find_element_by_id("joinname").send_keys("AutoJoinClause")
        driver.find_element_by_name("mapdesc").send_keys("Testing where clause")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        time.sleep(3)

        # Run Join
        driver.find_element_by_xpath("//*[text()='Run Join']").click()
        time.sleep(3)
        driver.find_element_by_name("columns").click()
        driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()
        time.sleep(15)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)



        time.sleep(6)


