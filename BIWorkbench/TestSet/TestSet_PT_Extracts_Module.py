import unittest
import HTMLTestRunner
import time

def creatsuite():
    testunit = unittest.TestSuite()
    test_dir = '../TestCases/PrimitiveTest'

    discover=unittest.defaultTestLoader.discover(test_dir,pattern='TC*.py',top_level_dir=None)

    for test_case in discover:
        print "test_case is %r" %test_case
        testunit.addTests(test_case)

    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = '../TestResults/'+now+'result.html'
filename = '../TestResults/testresult.html'
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='BI Workbench Testing',
    description='BI Workbench testing'
)

if __name__=='__main__':
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
