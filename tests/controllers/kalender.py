import unittest
from gluon.globals import Request, Session, Storage, Response
from testhelper import form_postvars

db = setupTestDb() # Use the test database for all tests


class KalenderController(unittest.TestCase):

    def setUp(self):
        request = Request({})


    def tearDown(self):
        db.kalender.truncate()
        db.wedstrijd.truncate()
        db.reeks.truncate()
        db.commit()


    def testOverzichtHeeftGeenKalenderBijLegeDb(self):
        """Geen kalenders bij lege database"""
        response = overzicht()
        self.assertEqual(0, len(response["kalenders"]))
