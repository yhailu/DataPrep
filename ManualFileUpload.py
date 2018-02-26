from BaseClasses.Locators import locators
from BaseClasses.Locators import locators


class ManualFileUpload():

    """Manual File Upload Keywords"""

    def __init__(self, driver):
        self.driver = driver

    def manualFileUpload(self, dir):
        """

        Args:
            dir: directory on your local of file you want to upload

        Returns: Void

        """
        manualFileUploadbutton = self.driver.find_element(locators['manual.file.upload.button'][0], locators['manual.file.upload.button'][1])
        manualFileUploadbutton.click()

        fileToUpload = self.driver.find_element(locators['file.upload'][0], locators['file.upload'][1])
        fileToUpload.send_keys(dir)

        uploadAll = self.driver.find_element(locators['upload.button'][0], locators['upload.button'][1]).click()
        alert = self.driver.switch_to.alert


    def close_driver_browser(self):
        """
        Summary: Close open browser and selenium driver will be closed as a
        process so no need to do this manually

        Returns: Void

        """
        self.driver.close()
        self.driver.quit()


