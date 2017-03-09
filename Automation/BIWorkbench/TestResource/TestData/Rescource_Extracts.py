import xml.sax
from TestResource.FunctionLibrary.CommonFunction import DataLoad
import GlobalParameter

"""
ExtractData class is used to load all test data from excel.
"""
class ExtractsData:
    def __init__(self,tc_name,row_run=1):
        data_load = DataLoad()
        row_number = data_load.common_excel_get_sepcify_row_by_number(tc_name,row_run,'Extract',GlobalParameter.data_file)
        self.default_role = data_load.common_excel_get_data_by_colname(row_number,'default_role','Extract',GlobalParameter.data_file)
        self.schema_name = data_load.common_excel_get_data_by_colname(row_number,'schema_name','Extract',GlobalParameter.data_file)
        self.table_name = data_load.common_excel_get_data_by_colname(row_number,'table_name','Extract',GlobalParameter.data_file)
        self.extract_name = data_load.common_excel_get_data_by_colname(row_number,'extract_name','Extract',GlobalParameter.data_file)
        self.subject_area = data_load.common_excel_get_data_by_colname(row_number,'subject_area','Extract',GlobalParameter.data_file)
        self.visibility = data_load.common_excel_get_data_by_colname(row_number,'visibility','Extract',GlobalParameter.data_file)
        self.publish_or_not = data_load.common_excel_get_data_by_colname(row_number,'publish_or_not','Extract',GlobalParameter.data_file)
        self.role_name = data_load.common_excel_get_data_by_colname(row_number,'role_name','Extract',GlobalParameter.data_file)
        self.success_message = data_load.common_excel_get_data_by_colname(row_number,'success_message','Extract',GlobalParameter.data_file)
        self.extract_delivery = data_load.common_excel_get_data_by_colname(row_number,'extract_delivery','Extract',GlobalParameter.data_file)
        self.schedule_type = data_load.common_excel_get_data_by_colname(row_number,'schedule_type','Extract',GlobalParameter.data_file)
        self.start_date = data_load.common_excel_get_data_by_colname(row_number,'start_date','Extract',GlobalParameter.data_file)
        self.run_time_hour = data_load.common_excel_get_data_by_colname(row_number,'run_time_hour','Extract',GlobalParameter.data_file)
        self.run_time_min = data_load.common_excel_get_data_by_colname(row_number,'run_time_min','Extract',GlobalParameter.data_file)
        self.number_of_occurences = data_load.common_excel_get_data_by_colname(row_number,'number_of_occurences','Extract',GlobalParameter.data_file)
        self.end_date = data_load.common_excel_get_data_by_colname(row_number,'end_date','Extract',GlobalParameter.data_file)
        self.patt_name = data_load.common_excel_get_data_by_colname(row_number,'patt_name','Extract',GlobalParameter.data_file)


"""
ExtractsObjects class is used to store all objects for extracts module.
"""
class ExtractsObjects(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self.CurrentData = ''
        self.userTenantsRoles = ''
        self.icon = ''
        self.createNewExtractButton = ''
        self.spansSchema = ''
        self.canvas = ''
        self.allColomns = ''
        self.extractName = ''
        self.extractDescription = ''
        self.subjectAreaAndVisibiity = ''
        self.publishCheckBox = ''
        self.RolesTab = ''
        self.allRoles = ''
        self.allCheckBoxes = ''
        self.extractDeliveryTab = ''
        self.deliveryButton = ''
        self.delivery = ''
        self.saveButton = ''
        self.confirmBox = ''
        self.okButton = ''
        self.extractScheduleTab = ''
        self.scheduleTypes = ''
        self.startDate = ''
        self.runTimeHour = ''
        self.runTimeMin = ''
        self.numberOfOccourence = ''
        self.endDate = ''
        self.weeklyDays = ''
        self.monthlyDay = ''


    def startElement(self,tag,attrs):
        self.CurrentData = tag

    def endElement(self,tag):
        self.CurrentData = ''

    def characters(self,content):
        content =content.strip().replace("\n","").replace("\r","")
        if self.CurrentData == 'userTenantsRoles':
            self.userTenantsRoles = content
        elif self.CurrentData == 'icon':
            self.icon = content
        elif self.CurrentData == 'spansSchema':
            self.spansSchema = content
        elif self.CurrentData == 'createNewExtractButton':
            self.createNewExtractButton = content
        elif self.CurrentData == 'canvas':
            self.canvas = content
        elif self.CurrentData == 'allColomns':
            self.allColomns = content
        elif self.CurrentData == 'extractName':
            self.extractName = content
        elif self.CurrentData == 'extractDescription':
            self.extractDescription = content
        elif self.CurrentData == 'subjectAreaAndVisibiity':
            self.subjectAreaAndVisibiity = content
        elif self.CurrentData == 'publishCheckBox':
            self.publishCheckBox = content
        elif self.CurrentData == 'RolesTab':
            self.RolesTab = content
        elif self.CurrentData == 'allRoles':
            self.allRoles = content
        elif self.CurrentData == 'allCheckBoxes':
            self.allCheckBoxes = content
        elif self.CurrentData == 'extractDeliveryTab':
            self.extractDeliveryTab = content
        elif self.CurrentData == 'deliveryButton':
            self.deliveryButton = content
        elif self.CurrentData == 'delivery':
            self.delivery = content
        elif self.CurrentData == 'saveButton':
            self.saveButton = content
        elif self.CurrentData == 'confirmBox':
            self.confirmBox = content
        elif self.CurrentData == 'okButton':
            self.okButton = content
        elif self.CurrentData == 'extractScheduleTab':
            self.extractScheduleTab = content
        elif self.CurrentData == 'scheduleTypes':
            self.scheduleTypes = content
        elif self.CurrentData == 'startDate':
            self.startDate = content
        elif self.CurrentData == 'runTimeHour':
            self.runTimeHour = content
        elif self.CurrentData == 'runTimeMin':
            self.runTimeMin = content
        elif self.CurrentData == 'numberOfOccourence':
            self.numberOfOccourence = content
        elif self.CurrentData == 'endDate':
            self.endDate = content
        elif self.CurrentData == 'weeklyDays':
            self.weeklyDays = content
        elif self.CurrentData == 'monthlyDay':
            self.monthlyDay = content