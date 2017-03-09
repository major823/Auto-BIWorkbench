import os
from datetime import *
files = os.listdir("C:\Python27\Automation\BIWorkbench\TestResults")


def file_clean(folder,file_start_with,days_before):
    file_removed = False
    for file in files:
        filepath = os.path.join(folder,file)
        if (datetime.now() - datetime.utcfromtimestamp(os.path.getctime(filepath))).days >= days_before and file.startswith(file_start_with):
            file_removed = True
            os.remove(filepath)
            print file+' is removed.'
    if file_removed == True:
        print 'Files cleaning is completed.'
    else:
        print 'Files are up to date. No file is removed.'

file_clean("C:\Python27\Automation\BIWorkbench\TestResults",'TestReport',1)


