from unittest import TestLoader, TestSuite , TextTestRunner
from HtmlTestRunner import HTMLTestRunner
from testSuiteVote.test_vote import TestVote
from testSuiteLogin.test_login import TestLogin
from testSuiteRegister.test_registration import TestRegistration


def create_test_suite():
    test_loader = TestLoader()
    test_suite = TestSuite()
    reg =test_loader.loadTestsFromTestCase(TestRegistration)
    log =test_loader.loadTestsFromTestCase(TestLogin)
    vot =test_loader.loadTestsFromTestCase(TestVote)
    test_suite.addTests([reg,log,vot])
    return test_suite

if __name__ == "__main__":
    suite = create_test_suite()
    runner = TextTestRunner(verbosity=2)
    runner = HTMLTestRunner()  
    runner.run(suite)