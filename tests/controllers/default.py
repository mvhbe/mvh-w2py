import unittest
from gluon.globals import Request, Session, Storage, Response
from testhelper import form_postvars

class DefaultController(unittest.TestCase):

    def setUp(self):
        request = Request()

    def testIndex(self):
        response = index()

        print "response :", response
        print "request : ", request