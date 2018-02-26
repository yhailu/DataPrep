import time

from BaseClasses.Locators import locators
from BaseClasses.singleton import Driver
from selenium.webdriver.common.by import By


class Unions():

    def __init__(self, driver):
        self.driver = driver

    def union(self):
        # Select Union tab
        driver = self.driver


        # select DBs and Tables
        # driver.find_element_by_xpath("//select[@name='sourceDB']/option[text()='open_automated']").click()
        # time.sleep(3)
        driver.find_element_by_xpath("//select[@name='sourceTable']/option[text()='autotable1']").click()
        driver.find_element_by_xpath("//select[@name='sourceTable']/option[text()='autotable2']").click()
        driver.find_element_by_xpath("//select[@name='sourceTable']/option[text()='autotable1']").click()
        # driver.find_element_by_xpath("//*[text()='Target Database']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='union 0']/div[2]/div[1]/div[2]/div/label/a").click()
        # driver.find_element_by_xpath("//*[@id='union 0']/div[2]/div[1]/div[2]/div/span/select/option[text()='open_automated']").click()
        driver.find_element_by_xpath("//*[@id='union 1']/div[2]/div[1]/div[2]/div[1]/label/a").click()
        # driver.find_element_by_xpath("//*[@id='union 1']/div[2]/div[1]/div[2]/div[1]/span/select/option[text()='open_automated']").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "//*[@id='union 1']/div[2]/div[1]/div[2]/div[2]/span/select/option[text()='autotable2']").click()

        # Clone and Delete Table
        driver.find_element_by_xpath("//*[text()='Clone Last Table']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='union 2']/div[1]/i[2]").click()
        time.sleep(3)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(3)

        # Saving Table
        driver.find_element_by_name("unionname").send_keys("Autounion1")
        driver.find_element_by_name("mapdesc").send_keys("Automated Union1")
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/footer/div/section/label[2]/input").click()
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/footer/div/div[3]/input").click()
        time.sleep(3)

        time.sleep(3)

        # Saving As Different Table
        driver.find_element_by_xpath(
            "//*[text()='Table in open_dan']").click()  # This is found in Table1 section
        driver.find_element_by_xpath(
            "//*[@id='union 1']/div[2]/div[1]/div[2]/div[2]/span/select/option[text()='autotable3']").click()
        driver.find_element_by_name("unionname").clear()
        driver.find_element_by_name("unionname").send_keys("Autounion2")
        driver.find_element_by_name("mapdesc").clear()
        driver.find_element_by_name("mapdesc").send_keys("Automated Union2")
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/footer/div/section/div/label[2]/i").click()
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/footer/div/div[3]/input").click()
        time.sleep(3)

        # Saving with a duplicate name
        driver.find_element_by_name("unionname").clear()
        driver.find_element_by_name("unionname").send_keys("Autounion1")
        driver.find_element_by_name("mapdesc").clear()
        driver.find_element_by_name("mapdesc").send_keys("Automated Union2")
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/footer/div/div[3]/input").click()
        time.sleep(3)

        time.sleep(3)

    def open_and_run(self, union):
        driver = self.driver

        # Open and run existing Union
        driver.find_element_by_xpath("//*[text()='Saved Unions']").click()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys(union)
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr/td[6]/button[1]").click()
        time.sleep(3)
        driver.find_element_by_css_selector("button.btn.btn-default.ng-scope").click()
        time.sleep(3)
        driver.find_element_by_name("columns").click()
        driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()
        time.sleep(15)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)

    def delete_union(self, union):
        # Delete Union
        driver = self.driver
        driver.find_element_by_xpath("//*[text()='Saved Unions']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys(union)
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr/td[6]/button[3]").click()
        alert = driver.switch_to.alert
        alert.accept()

    def unions_regression(self):
        driver = self.driver
        driver.find_element_by_xpath("//select[@name='sourceDB']/option[text()='open_automated']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//select[@name='sourceTable']/option[text()='autotable1']").click()
        driver.find_element_by_xpath("//select[@name='sourceTable']/option[text()='autotable2']").click()
        driver.find_element_by_xpath("//select[@name='sourceTable']/option[text()='autotable1']").click()
        # driver.find_element_by_xpath("//*[text()='Target Database']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='union 0']/div[2]/div[1]/div[2]/div/label/a").click()
        driver.find_element_by_xpath(
            "//*[@id='union 0']/div[2]/div[1]/div[2]/div/span/select/option[text()='open_automated']").click()
        driver.find_element_by_xpath("//*[@id='union 1']/div[2]/div[1]/div[2]/div[1]/label/a").click()
        driver.find_element_by_xpath(
            "//*[@id='union 1']/div[2]/div[1]/div[2]/div[1]/span/select/option[text()='open_automated']").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "//*[@id='union 1']/div[2]/div[1]/div[2]/div[2]/span/select/option[text()='autotable2']").click()

        # Clone and Delete Table
        driver.find_element_by_xpath("//*[text()='Clone Last Table']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='union 2']/div[1]/i[2]").click()
        time.sleep(3)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(3)

        # Saving Table
        driver.find_element_by_name("unionname").send_keys("Autounion1")
        driver.find_element_by_name("mapdesc").send_keys("Automated Union1")
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/footer/div/section/label[2]/input").click()
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/footer/div/div[3]/input").click()
        time.sleep(3)
        # driver.get_screenshot_as_file("C:\\Automation\\Screenshots\\Regression\\UnionSuccessfullCreate.png")
        time.sleep(3)

        # Saving As Different Table
        # driver.find_element_by_xpath('id("union 1")/div[2]/div[1]/div[2]/div[2]/label[1]/a[1]').click()
        driver.find_element(By.LINK_TEXT, 'Table in open_automated').click()
        driver.find_element_by_xpath(
            "//*[@id='union 1']/div[2]/div[1]/div[2]/div[2]/span/select/option[text()='autotable3']").click()
        driver.find_element_by_name("unionname").clear()
        driver.find_element_by_name("unionname").send_keys("Autounion2")
        driver.find_element_by_name("mapdesc").clear()
        driver.find_element_by_name("mapdesc").send_keys("Automated Union2")
        driver.find_element_by_xpath(
            'id("wid-id-0")/div[1]/div[2]/div[1]/footer[1]/div[1]/section[1]/div[1]/label[2]').click()
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/footer/div/div[3]/input").click()
        time.sleep(3)

        # Saving with a duplicate name
        driver.find_element_by_name("unionname").clear()
        driver.find_element_by_name("unionname").send_keys("Autounion1")
        driver.find_element_by_name("mapdesc").clear()
        driver.find_element_by_name("mapdesc").send_keys("Automated Union2")
        driver.find_element_by_xpath("//*[@id='wid-id-0']/div/div[2]/div/footer/div/div[3]/input").click()
        time.sleep(3)
        # driver.get_screenshot_as_file("C:\\Automation\\Screenshots\\Regression\\UnionDuplicateName.png")
        time.sleep(3)

        # Open and run existing Union
        driver.find_element_by_xpath("//*[text()='Saved Unions']").click()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys("autounion1")
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr/td[6]/button[1]").click()
        time.sleep(3)
        driver.find_element_by_css_selector("button.btn.btn-default.ng-scope").click()
        time.sleep(3)
        driver.find_element_by_name("columns").click()
        driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()
        time.sleep(15)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)

        # Delete Union
        driver.find_element_by_xpath("//*[text()='Saved Unions']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").send_keys("autounion2")
        driver.find_element_by_xpath("//*[@id='columnListTbl']/tbody/tr/td[6]/button[3]").click()

        time.sleep(5)
        alert = driver.switch_to.alert
        alert.accept()
        driver.find_element_by_xpath("//*[@id='columnListTbl']/thead/tr/th[1]/div/input").clear()
        time.sleep(3)

    def close_driver_broswer(self):
        """Close open browser and selenium driver will be closed as a
        process so no need to do this manually
        """
        self.driver.close()
        self.driver.quit()