#coding=utf-8
from selenium import webdriver
import unittest
import TestResource.TestData.GlobalParameter
from TestResource.ObjectRepository.PO_Extracts import POExtracts
from BusinessComponent.BC_PT_Extracts import PrimitiveTestExtracts
from time import *


class TestExtract(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_create_template_extract_onetime(self):
        pt_extracts = PrimitiveTestExtracts(self.driver)
        po_extracts = POExtracts(self.driver)
        po_extracts.open_url(TestResource.TestData.GlobalParameter.url)
        sleep(5)
        # pt_extracts.is_userTenantsRoles_displayed()
        pt_extracts.is_icon_displayed()
        po_extracts.click_extracts_icon()
        sleep(5)
        pt_extracts.is_createNewExtractButton_displayed()
        po_extracts.click_createNewExtract_button()
        sleep(5)
        pt_extracts.is_canvas_displayed()
        pt_extracts.is_extractName_displayed()
        pt_extracts.is_extractDescription_displayed()
        pt_extracts.is_subjectAreaAndVisibiity_displayed()
        pt_extracts.is_RolesTab_displayed()
        po_extracts.click_roles_tab()
        sleep(5)
        pt_extracts.is_allRoles_displayed()
        pt_extracts.is_allCheckBoxes_displayed()
        pt_extracts.is_extractDeliveryTab_displayed()
        po_extracts.click_delivery_tab()
        sleep(5)
        pt_extracts.is_deliveryButton_displayed()
        po_extracts.click_delivery_button()
        pt_extracts.is_delivery_displayed()
        pt_extracts.is_extractScheduleTab_displayed()
        po_extracts.click_schedule_tab()
        sleep(5)
        pt_extracts.is_spansSchema_displayed()
        pt_extracts.is_startDate_displayed()
        pt_extracts.is_runTimeHour_displayed()
        pt_extracts.is_runTimeMin_displayed()
        pt_extracts.is_numberOfOccourence_displayed()
        pt_extracts.is_endDate_displayed()
        pt_extracts.is_weeklyDays_displayed()
        pt_extracts.is_monthlyDay_displayed()
        pt_extracts.is_saveButton_displayed()



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
