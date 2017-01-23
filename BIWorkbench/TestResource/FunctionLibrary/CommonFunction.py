import xlrd
import re
import  xml.sax
# import ExtractsPage
from selenium import webdriver
from selenium.webdriver.support.ui import Select
object_file = "C:\Python27\Automation\BIWorkbench\TestResource\TestData\object.xml"


# extracts_data = ExtractsPage.ExtractsData()
class Common:
    def __init__(self,driver):
        self.driver = driver

    def Login(self,url):
        self.driver.get(url)



class DataLoad:

    def common_open_excel(self,file):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception, e:
            print str(e)

    # get the rows by Test case ID, if not found, return the warning message and then exit the script
    def common_excel_get_rows_by_tcid(self,tcid,by_name,file):
        data = self.common_open_excel(file)
        table = data.sheet_by_name(by_name)
        nrows = table.nrows #rows number
        ncols = table.ncols #columns number
        firstcolvalues = table.col_values(0) #data in columns 1
        p = re.compile(r'=')
        rows=0
        for i in range(1,nrows):
            ntc = p.split(firstcolvalues[i])[0]
            if ntc == tcid:
                rows = str(rows)+"="+str(i)
                continue
            elif i == nrows-1 and rows == 0 and ntc != tcid:
                print "can not find the row by TC name, please enter the correct TC name"
                exit()
        return rows

    # Get the specify row by number in on Test case.
    def common_excel_get_sepcify_row_by_number(self,tcid,number,by_name,file):
        rows = self.common_excel_get_rows_by_tcid(tcid,by_name,file)
        p = re.compile(r"=")
        rownumb = p.split(rows)
        return rownumb[number]


    #Get the test data by column name, if not found, pop up error message and exit the script
    def common_excel_get_data_by_colname(self,row,colname,by_name,file):
        data = self.common_open_excel(file)
        table = data.sheet_by_name(by_name)
        nrows = table.nrows #rows number
        ncols = table.ncols #columns number
        firstrowvalues = table.row_values(0) #data in row 1
        for i in range(1,ncols):
            if firstrowvalues[i] == colname:
                rowindex = i
                return table.cell(int(row),rowindex).value
            elif i == ncols - 1 and firstrowvalues[ncols - 1] != colname:
                print "can not find the column by column name, please enter the correct column name"
                exit()
