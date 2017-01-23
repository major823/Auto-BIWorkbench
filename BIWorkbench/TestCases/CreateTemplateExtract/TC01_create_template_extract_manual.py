#coding=utf-8
from selenium import webdriver
import unittest
import BC_Extracts
from Rescource_Extracts import ExtractsData
import GlobalParameter
tc_name = 'TC01_create_template_extract_manual'

class TestExtract(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_create_template_extract_manual(self):
        extracts_data = ExtractsData(tc_name)
        bc_extracts = BC_Extracts.BC_Extracts(self.driver)
        bc_extracts.pre_create_extract(GlobalParameter.url,extracts_data.default_role)
        bc_extracts.create_extract_select_table_colomn(extracts_data.schema_name,extracts_data.table_name)
        bc_extracts.create_extract_fill_properties(extracts_data.extract_name,extracts_data.subject_area,extracts_data.visibility,extracts_data.publish_or_not)
        bc_extracts.create_extract_select_roles(extracts_data.role_name)
        bc_extracts.create_extract_select_delivery(extracts_data.extract_delivery)
        bc_extracts.create_extract_set_schedule_manual(extracts_data.schedule_type)
        bc_extracts.post_create_extract(extracts_data.success_message)


        # driver.find_element_by_partial_link_text('Save').click()
        # text = driver.find_element_by_css_selector('#alert-info-label').text
        # try: self.assertEqual(extracts_data.success_message, text)
        # except AssertionError as e: self.verificationErrors.append(str(e))
        # driver.find_element_by_css_selector('#alertInfoOKWithFunc').click()
        # Select(driver.find_element_by_css_selector('#DDL_UserTenantsRoles')).select_by_visible_text('UAT Testers')
        # sleep(5)
        # driver.find_element_by_css_selector('a[title="Extracts"]').click()
        # extracts = driver.find_elements_by_css_selector('span[data-bind="text: extractName"]')
        # for extract in extracts:
        #     try: self.assertEqual(extract_name, extract.text)
        #     except AssertionError as e: self.verificationErrors.append(str(e))
        #
        # Select(driver.find_element_by_css_selector('#DDL_UserTenantsRoles')).select_by_visible_text('ebi EIT')
        # sleep(5)
        # driver.find_element_by_css_selector('a[title="Extracts"]').click()
        # extracts = driver.find_elements_by_css_selector('span[data-bind="text: extractName"]')
        # for extract in extracts:
        #     try: self.assertEqual(extract_name, extract.text)
        #     except AssertionError as e: self.verificationErrors.append(str(e))
        #
        #
        # Select(driver.find_element_by_css_selector('#DDL_UserTenantsRoles')).select_by_visible_text('TestSAdmin')
        # sleep(5)
        # driver.find_element_by_css_selector('a[title="Extracts"]').click()
        # extracts = driver.find_elements_by_css_selector('span[data-bind="text: extractName"]')
        # buttons = driver.find_elements_by_css_selector('button[class="fa fa-trash-o"]')
        # i = 0
        # for extract in extracts:
        #     if extract.text == ExtractName:
        #         buttons.pop(i).click()
        #         driver.find_element_by_css_selector('#DeleteExtractDefinitionDisclaimer * button.btn.btn-primary').click()
        #         break
        #     else:
        #         i = i+1
        # for i in (range(len(extracts)-1,0)):

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
    # runner = unittest.TextTestRunner()
    # test_suite=unittest.TestSuite()
    # test_suite.addTest(TestExtract("test_create_template_extract_manual"))
    # filename = 'C:\\Python27\\Automation\\BIWorkbench\\TestResults\\testresult.html'
    # fp = file(filename, 'wb')
    # runner =HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='BI Workbench Test Report',
    #     description='Test Execution Status')
    # runner.run(test_suite)
    # fp.close()
