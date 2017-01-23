from time import *
import re
from datetime import *
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.common.action_chains import ActionChains
import Rescource_Extracts
from BasePage import BasePage
import xml.sax
import GlobalParameter


class POExtracts(BasePage):
    extracts_objects = Rescource_Extracts.ExtractsObjects()
    saxParser = xml.sax.make_parser()
    saxParser.setContentHandler(extracts_objects)
    saxParser.parse(GlobalParameter.object_file)

    def open_url(self,url):
        self.open(url)

    def click_extracts_icon(self):
        self.driver.find_element_by_css_selector(self.extracts_objects.icon).click()

    def select_tenant_role(self,default_role):
        Select(self.driver.find_element_by_css_selector(self.extracts_objects.userTenantsRoles)).select_by_visible_text(default_role)

    def click_createNewExtract_button(self):
        self.driver.find_element_by_css_selector(self.extracts_objects.createNewExtractButton).click()

    def select_specific_schema(self,schema_name):
        i = 0
        spans_schema = self.driver.find_elements_by_css_selector(self.extracts_objects.spansSchema)
        for span_schema in spans_schema:
            if span_schema.text == schema_name:
                spans_schema[i-2].click()
                break
            else:
                i = i +1


    def drag_and_drop_table(self,table_name):
        element = self.driver.find_element_by_css_selector('a[title='+table_name+']')
        target = self.driver.find_element_by_css_selector(self.extracts_objects.canvas)
        ActionChains(self.driver).move_to_element(target).perform()
        ActionChains(self.driver).drag_and_drop(element,target).perform()

    def select_colomn_in_table(self):
        columns = self.driver.find_elements_by_css_selector(self.extracts_objects.allColomns)
        columns[random.randint(0,len(columns)-1)].click()

    def enter_extract_name(self,extract_name):
        ExtractName = 'Auto-'+extract_name + '-'+ctime()
        self.driver.find_element_by_css_selector(self.extracts_objects.extractName).send_keys(ExtractName)

    def enter_extract_description(self,extract_name):
        ExtractDescription = extract_name + ' - '+ctime()
        self.driver.find_element_by_css_selector(self.extracts_objects.extractDescription).send_keys(ExtractDescription)

    def select_subject_area(self,subject_area):
        subjectAreaAndVisibiity = self.driver.find_elements_by_css_selector(self.extracts_objects.subjectAreaAndVisibiity)
        if subject_area != '':
            Select(subjectAreaAndVisibiity[0]).select_by_visible_text(subject_area)

    def select_visibility(self,visibility):
        subjectAreaAndVisibiity = self.driver.find_elements_by_css_selector(self.extracts_objects.subjectAreaAndVisibiity)
        if visibility != '':
            Select(subjectAreaAndVisibiity[1]).select_by_visible_text(visibility)

    def check_publish_or_not(self,publish_or_not):
        if publish_or_not == 'Yes':
            self.driver.find_element_by_css_selector(self.extracts_objects.publishCheckBox).click()

    def click_roles_tab(self):
        self.driver.find_element_by_link_text(self.extracts_objects.RolesTab).click()

    def select_specific_role(self,role_name):
        spans = self.driver.find_elements_by_css_selector(self.extracts_objects.allRoles)
        checkboxes = self.driver.find_elements_by_css_selector(self.extracts_objects.allCheckBoxes)
        i = 0
        for span in spans:
            if span.text == role_name:
                checkboxes[i].click()
                break
            else:
                i = i + 1

    def click_delivery_tab(self):
        self.driver.find_element_by_link_text(self.extracts_objects.extractDeliveryTab).click()

    def click_delivery_button(self):
        self.driver.find_element_by_css_selector(self.extracts_objects.deliveryButton).click()

    def select_extract_delivery(self,extract_delivery):
        Select(self.driver.find_element_by_css_selector(self.extracts_objects.delivery)).select_by_visible_text(extract_delivery)

    def click_schedule_tab(self):
        self.driver.find_element_by_link_text(self.extracts_objects.extractScheduleTab).click()

    def get_schedule_type(self,type_order):
        schedule_types = self.driver.find_elements_by_css_selector(self.extracts_objects.scheduleTypes)
        return schedule_types[type_order]

    def select_specific_schedule_type(self,schedule_type):
        if schedule_type == 'Manual':
            self.get_schedule_type(0).click()
        elif schedule_type == 'One Time':
            self.get_schedule_type(1).click()
        elif schedule_type == 'Daily':
            self.get_schedule_type(2).click()
        elif schedule_type == 'Weekly':
            self.get_schedule_type(3).click()
        elif schedule_type == 'Monthly':
            self.get_schedule_type(4).click()

    def enter_start_date(self,start_date=date.today().strftime("%m-%d-%Y ")):
        self.driver.find_element_by_xpath(self.extracts_objects.startDate).clear()
        self.driver.find_element_by_xpath(self.extracts_objects.startDate).send_keys(start_date)

    def enter_run_time_hour(self,run_time_hour=strftime("%H", localtime()) ):
        self.driver.find_element_by_css_selector(self.extracts_objects.runTimeHour).send_keys(run_time_hour)

    def enter_run_time_min(self,run_time_min=strftime("%M", localtime()) ):
        self.driver.find_element_by_css_selector(self.extracts_objects.runTimeMin).send_keys(run_time_min)

    def select_end_after(self):
        self.get_schedule_type(5).click()

    def enter_number_of_occurences(self,number_of_occurences):
        sleep(3)
        self.driver.find_element_by_xpath(self.extracts_objects.numberOfOccourence).clear()
        self.driver.find_element_by_xpath(self.extracts_objects.numberOfOccourence).send_keys(number_of_occurences)

    def select_end_by(self):
        self.get_schedule_type(6).click()

    def enter_end_date(self,end_date=(date.today()+timedelta(days=1)).strftime("%m-%d-%Y")):
        self.driver.find_element_by_xpath(self.extracts_objects.endDate).clear()
        self.driver.find_element_by_xpath(self.extracts_objects.endDate).send_keys(end_date)

    def select_weekly_days(self,):
        weekly_days_objects = self.driver.find_elements_by_xpath(self.extracts_objects.weeklyDays)
        random_weekly_days_objects = random.sample(weekly_days_objects,random.randint(1,len(weekly_days_objects)))
        for weekly_days_object in random_weekly_days_objects:
           weekly_days_object.click()

    def select_monthly_day(self):
        Select(self.driver.find_element_by_xpath(self.extracts_objects.monthlyDay)).select_by_visible_text(str(random.randint(1,31)))


    def click_save_button(self):
        sleep(2)
        self.driver.find_element_by_partial_link_text(self.extracts_objects.saveButton).click()

    def check_success_message(self,success_message):
        text_confirm = self.driver.find_element_by_css_selector(self.extracts_objects.confirmBox).text
        if text_confirm == success_message:
            print 'testing is passed'
        else:
            print 'testing is failed'

    def click_success_ok_button(self):
        sleep(2)
        self.driver.find_element_by_css_selector(self.extracts_objects.okButton).click()

    def click_delete_button(self):
        extracts = self.driver.find_elements_by_xpath('//*[@id="existingExtractsTab"]/table/tbody/tr[12]/td[4]/span')
        buttons = self.driver.find_elements_by_xpath('button[class="fa fa-trash-o"]')

        i = 0
        for extract in extracts:
            if re.match('Auto',extract.text):
                extract
                buttons[i].click()
                self.driver.find_element_by_css_selector('#DeleteExtractDefinitionDisclaimer * button.btn.btn-primary').click()
                self.driver.find_element_by_css_selector('#alertInfoOKWithFunc').click()
                i = i + 1
                sleep(2)

            else:
                 i = i + 1