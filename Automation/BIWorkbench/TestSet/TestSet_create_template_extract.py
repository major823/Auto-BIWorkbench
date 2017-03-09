import unittest
import HTMLTestRunner
import time
import os
def creatsuite():
    testunit = unittest.TestSuite()
    test_dir = '../TestCases/CreateTemplateExtract'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='TC*.py',top_level_dir=None)
    for test_case in discover:
        print test_case
        testunit.addTests(test_case)
    return testunit
now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = '../TestResults/'+now+'result.html'
filename = '../TestResults/'+'TestReport for '+os.path.basename(__file__).split('.',1)[0]+now+'.html'
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='BI Workbench Testing',
    description='BI Workbench testing'
)

if __name__ == '__main__':
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
