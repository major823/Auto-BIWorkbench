from selenium import webdriver


class CreateExtract:

    def __init__(self,selenium_driver):
        self.driver = selenium_driver

    def select_specific_schema(self,schema_name):
        i = 0
        # driver = self.driver
        spans_schema = self.driver.find_elements_by_css_selector('#tree * span')
        for span_schema in spans_schema:
            if span_schema.text == schema_name:
                spans_schema.pop(i-2).click()
                break
            else:
                i = i +1

    def select_specific_role(self,allRoles,allCheckBoxes,role_name):
        spans = self.driver.find_elements_by_css_selector(allRoles)
        checkboxes = self.driver.find_elements_by_css_selector(allCheckBoxes)
        i = 0
        for span in spans:
            if span.text == role_name:
                checkboxes.pop(i).click()
                break
            else:
                i = i + 1