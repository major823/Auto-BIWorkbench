#coding=utf-8
from selenium import webdriver
import unittest
import BC_Extracts
from Rescource_Extracts import ExtractsData
import GlobalParameter
tc_name = 'TC04_create_template_extract_weekly'


class TestExtract(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_create_template_extract_onetime(self):
        extracts_data = ExtractsData(tc_name)
        bc_extracts = BC_Extracts.BC_Extracts(self.driver)
        bc_extracts.pre_create_extract(GlobalParameter.url,extracts_data.default_role)
        bc_extracts.create_extract_select_table_colomn(extracts_data.schema_name,extracts_data.table_name)
        bc_extracts.create_extract_fill_properties(extracts_data.extract_name,extracts_data.subject_area,extracts_data.visibility,extracts_data.publish_or_not)
        bc_extracts.create_extract_select_roles(extracts_data.role_name)
        bc_extracts.create_extract_select_delivery(extracts_data.extract_delivery)
        bc_extracts.create_extract_set_schedule_weekly_end_by(extracts_data.schedule_type)
        bc_extracts.post_create_extract(extracts_data.success_message)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
