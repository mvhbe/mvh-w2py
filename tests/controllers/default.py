import unittest
from gluon.globals import Request, Session, Storage, Response
from testhelper import form_postvars

db = setupTestDb() # Use the test database for all tests

class DefaultController(unittest.TestCase):

    def setUp(self):
        request = Request({})

    def testIndex(self):
        """Geen wedstrijden aanwezig"""
        response = index()

        self.assertEqual(0, len(response["wedstrijden"]))
        #print "response :", response
        #print "request : ", request