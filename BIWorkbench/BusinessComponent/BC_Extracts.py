from time import *
from PO_Extracts import POExtracts


class BC_Extracts():
    def __init__(self,driver):
        self.driver = driver
        self.verificationErrors = []
        self.accept_next_alert = True
        self.po_extracts = POExtracts(driver)

    def pre_create_extract(self,url,default_role):
        self.po_extracts.open_url(url)
        self.po_extracts.select_tenant_role(default_role)
        self.po_extracts.click_extracts_icon()
        sleep(4)
        self.po_extracts.click_createNewExtract_button()
        sleep(2)

    def create_extract_select_table_colomn(self,schema_name,table_name):
        self.po_extracts.select_specific_schema(schema_name)
        sleep(1)
        self.po_extracts.drag_and_drop_table(table_name)
        self.po_extracts.select_colomn_in_table()

    def create_extract_fill_properties(self,extract_name,subject_area,visibility,publish_or_not):
        self.po_extracts.enter_extract_name(extract_name)
        self.po_extracts.enter_extract_description(extract_name)
        self.po_extracts.select_subject_area(subject_area)
        self.po_extracts.select_visibility(visibility)
        self.po_extracts.check_publish_or_not(publish_or_not)

    def create_extract_select_roles(self,role_name):
        self.po_extracts.click_roles_tab()
        self.po_extracts.select_specific_role(role_name)

    def create_extract_select_delivery(self,extract_delivery):
        self.po_extracts.click_delivery_tab()
        self.po_extracts.click_delivery_button()
        self.po_extracts.select_extract_delivery(extract_delivery)

    def create_extract_set_schedule_manual(self,schedule_type):
        self.po_extracts.click_schedule_tab()
        self.po_extracts.select_specific_schedule_type(schedule_type)

    def create_extract_set_schedule_onetime(self,schedule_type,run_time_hour,run_time_min):
        self.po_extracts.click_schedule_tab()
        self.po_extracts.select_specific_schedule_type(schedule_type)
        self.po_extracts.enter_start_date()
        self.po_extracts.enter_run_time_hour(run_time_hour)
        self.po_extracts.enter_run_time_min(run_time_min)

    def create_extract_set_schedule_daily_end_after(self,schedule_type,number_of_occurences):
        self.po_extracts.click_schedule_tab()
        self.po_extracts.select_specific_schedule_type(schedule_type)
        self.po_extracts.select_end_after()
        self.po_extracts.enter_number_of_occurences(number_of_occurences)


    def create_extract_set_schedule_weekly_end_by(self,schedule_type):
        self.po_extracts.click_schedule_tab()
        self.po_extracts.select_specific_schedule_type(schedule_type)
        self.po_extracts.select_weekly_days()
        self.po_extracts.select_end_by()
        self.po_extracts.enter_end_date()

    def create_extract_set_schedule_monthly(self,schedule_type):
        self.po_extracts.click_schedule_tab()
        self.po_extracts.select_specific_schedule_type(schedule_type)
        self.po_extracts.select_monthly_day()

    def post_create_extract(self,success_message):
        self.po_extracts.click_save_button()
        self.po_extracts.check_success_message(success_message)
        self.po_extracts.click_success_ok_button()

    def navigate_to_extracts_page(self,url,default_role):
        self.po_extracts.open_url(url)
        self.po_extracts.select_tenant_role(default_role)
        self.po_extracts.click_extracts_icon()
        sleep(4)

    def delete_auto_extracts(self):
        self.po_extracts.click_delete_button()
