#coding=utf-8
from selenium import webdriver
import unittest
import BusinessComponent.BC_Extracts
from TestResource.TestData.Rescource_Extracts import ExtractsData
import TestResource.TestData.GlobalParameter
tc_name = 'TC06_delete_template_extract'

class TestExtract(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_create_template_extract_manual(self):
        extracts_data = ExtractsData(tc_name)
        bc_extracts = BusinessComponent.BC_Extracts.BC_Extracts(self.driver)
        bc_extracts.navigate_to_extracts_page(TestResource.TestData.GlobalParameter.url,extracts_data.default_role)
        bc_extracts.delete_auto_extracts(extracts_data.patt_name)


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
