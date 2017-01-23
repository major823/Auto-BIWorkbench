import xlrd
import re
import  xml.sax
from Rescource_Extracts import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
object_file = "C:\Python27\Automation\BIWorkbench\TestResource\TestData\object.xml"
saxParser = xml.sax.make_parser()
extracts_objects = ExtractsObjects()
saxParser.setContentHandler(extracts_objects)
saxParser.parse(object_file)
class Home:
    def __init__(self,driver):
        self.driver = driver
    def select_tenant_role(self,default_role):
        Select(self.driver.find_element_by_css_selector(extracts_objects.userTenantsRoles)).select_by_visible_text(default_role)
    def select_icon_link(self):
        self.driver.find_element_by_css_selector(extracts_objects.icon).click()