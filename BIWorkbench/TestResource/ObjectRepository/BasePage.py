from selenium.webdriver.common.by import By
from selenium import webdriver
class BasePage:
    def __init__(self,selenium_driver):
        self.driver = selenium_driver

    def find_element(self,loc):
        return self.driver.find_element_by_css_selector(loc)

    # def find_element_xpath(self,loc):
    #     return self.driver.find_element_by_xpath(loc)

    def find_elements(self,loc):
        return self.driver.find_elements(loc)

    def open(self,url):
        self.driver.get(url)

    def is_element_displayed(self,page_object,css_object,selector_type='css_selector'):
        if selector_type == 'css_selector':
            if self.driver.find_element_by_css_selector(css_object):
                print page_object + " element is displayed"
            else:
                print page_object + " element is NOT displayed"

        elif selector_type == 'xpath':
            if self.driver.find_element_by_xpath(css_object):
                print page_object + " element is displayed"
            else:
                print page_object + " element is NOT displayed"

        elif selector_type == 'xpaths':
            if self.driver.find_elements_by_xpath(css_object):
                print page_object + " element is displayed"
            else:
                print page_object + " element is NOT displayed"

        elif selector_type == 'css_selectors':
            if self.driver.find_elements_by_css_selector(css_object):
                print page_object + " element is displayed"
            else:
                print page_object + " element is NOT displayed"

        elif selector_type == 'link':
            if self.driver.find_element_by_link_text(css_object):
                print page_object + " element is displayed"
            else:
                print page_object + " element is NOT displayed"

        elif selector_type == 'partial_link':
            if self.driver.find_element_by_partial_link_text(css_object):
                print page_object + " element is displayed"
            else:
                print page_object + " element is NOT displayed"


    def send_keys(self,loc,value, clear_first=False):
        try:
            # loc = getattr(self, '_%s' % loc)
            if clear_first:
                self.find_element(loc).clear()
                self.find_element(loc).send_keys(value)
        except AttributeError:
            print '%s page does not have "%s" locator' %(self,loc)