from TestResource.ObjectRepository.BasePage import BasePage
import TestResource.TestData.Rescource_Extracts
import  xml.sax
object_file = "C:\Python27\Automation\BIWorkbench\TestResource\TestData\objectExtracts.xml"

class PrimitiveTestExtracts(BasePage):
    extracts_objects = TestResource.TestData.Rescource_Extracts.ExtractsObjects()
    saxParser = xml.sax.make_parser()
    saxParser.setContentHandler(extracts_objects)
    saxParser.parse(object_file)
    def is_icon_displayed(self):
        self.is_element_displayed('Extracts icon',self.extracts_objects.icon)

    def is_userTenantsRoles_displayed(self):
        self.is_element_displayed('userTenantsRoles',self.extracts_objects.userTenantsRoles)

    def is_createNewExtractButton_displayed(self):
        self.is_element_displayed('createNewExtractButton',self.extracts_objects.createNewExtractButton)

    def is_spansSchema_displayed(self):
        self.is_element_displayed('spansSchema',self.extracts_objects.spansSchema,'css_selectors')

    def is_canvas_displayed(self):
        self.is_element_displayed('canvas',self.extracts_objects.canvas)

    def is_extractName_displayed(self):
        self.is_element_displayed('extractName',self.extracts_objects.extractName)

    def is_extractDescription_displayed(self):
        self.is_element_displayed('extractDescription',self.extracts_objects.extractDescription)
    def is_subjectAreaAndVisibiity_displayed(self):
        self.is_element_displayed('subjectAreaAndVisibiity',self.extracts_objects.subjectAreaAndVisibiity,'css_selectors')
    def is_publishCheckBox_displayed(self):
        self.is_element_displayed('publishCheckBox',self.extracts_objects.publishCheckBox)
    def is_RolesTab_displayed(self):
        self.is_element_displayed('RolesTab',self.extracts_objects.RolesTab,'link')
    def is_allRoles_displayed(self):
        self.is_element_displayed('allRoles',self.extracts_objects.allRoles,'css_selectors')
    def is_allCheckBoxes_displayed(self):
        self.is_element_displayed('allCheckBoxes',self.extracts_objects.allCheckBoxes,'css_selectors')
    def is_extractDeliveryTab_displayed(self):
        self.is_element_displayed('extractDeliveryTab',self.extracts_objects.extractDeliveryTab,'link')
    def is_deliveryButton_displayed(self):
        self.is_element_displayed('deliveryButton',self.extracts_objects.deliveryButton)
    def is_delivery_displayed(self):
        self.is_element_displayed('delivery',self.extracts_objects.delivery)
    def is_extractScheduleTab_displayed(self):
        self.is_element_displayed('extractScheduleTab',self.extracts_objects.extractScheduleTab,'link')
    def is_scheduleTypes_displayed(self):
        self.is_element_displayed('scheduleTypes',self.extracts_objects.scheduleTypes)

    def is_startDate_displayed(self):
        self.is_element_displayed('startDate',self.extracts_objects.startDate,'xpath')
    def is_runTimeHour_displayed(self):
        self.is_element_displayed('runTimeHour',self.extracts_objects.runTimeHour)
    def is_runTimeMin_displayed(self):
        self.is_element_displayed('runTimeMin',self.extracts_objects.runTimeMin)
    def is_numberOfOccourence_displayed(self):
        self.is_element_displayed('numberOfOccourence',self.extracts_objects.numberOfOccourence,'xpath')
    def is_endDate_displayed(self):
        self.is_element_displayed('endDate',self.extracts_objects.endDate,'xpath')
    def is_weeklyDays_displayed(self):
        self.is_element_displayed('weeklyDays',self.extracts_objects.weeklyDays,'xpaths')
    def is_monthlyDay_displayed(self):
        self.is_element_displayed('monthlyDay',self.extracts_objects.monthlyDay,'xpath')
    def is_saveButton_displayed(self):
        self.is_element_displayed('saveButton',self.extracts_objects.saveButton,'partial_link')
