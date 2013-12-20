import datetime
import unittest
from gluon.globals import Request, Session, Storage, Response
from testhelper import form_postvars

db = setupTestDb() # Use the test database for all tests

vandaag = datetime.date(datetime.datetime.now())
een_maand_geleden = vandaag - 30
een_maand_verder = vandaag + 30

def niewe_wedstrijd(datum):
    pass

class DefaultController(unittest.TestCase):

    def setUp(self):
        request = Request({})

    def testIndexGeeftGeenWedstrijdenTerugBijLegeDb(self):
        """Geen data aanwezig"""
        response = index()

        self.assertEqual(0, len(response["wedstrijden"]))


    def testIndexGeeftWedstrijdHuidigeMaandTerug(self):
        """Wedstrijddatum huidige maand wordt opgehaald"""
        pass


    def testIndexGeeftWedstrijdVolgendeMaandNietTerug(self):
        """Wedstrijddatum volgende maand wordt niet opgehaald"""
        pass


    def testIndexGeeftWedstrijdVorigeMaandNietTerug(self):
        """Wedstrijddatum vorige maand wordt niet opgehaald"""
        pass
