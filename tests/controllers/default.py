import datetime
import unittest
from dateutil import relativedelta
from gluon.globals import Request, Session, Storage, Response
from testhelper import form_postvars

db = setupTestDb() # Use the test database for all tests

VANDAAG = datetime.datetime.now().date()
EEN_MAAND_GELEDEN = VANDAAG - relativedelta.relativedelta(months=-1)
EEN_MAAND_VERDER = VANDAAG + relativedelta.relativedelta(months=+1)

def nieuweWedstrijd(kalender=1,datum=VANDAAG,
                    omschrijving="Leden wedstrijd " +
                                 VANDAAG.strftime("%d/%m/%Y")):
    db.wedstrijd.insert(kalender=kalender, datum=datum,
                            omschrijving=omschrijving)
    db.commit()


class DefaultController(unittest.TestCase):

    def setUp(self):
        request = Request({})


    def tearDown(self):
        db.wedstrijd.delete()
        db.commit()


    def testIndexGeeftGeenWedstrijdenTerugBijLegeDb(self):
        """Geen data aanwezig"""
        response = index()
        self.assertEqual(0, len(response["wedstrijden"]))


    def testIndexGeeftWedstrijdHuidigeMaandTerug(self):
        """Wedstrijddatum huidige maand wordt opgehaald"""
        nieuweWedstrijd()
        self.assertEqual(1, len(response["wedstrijden"]))


    def testIndexGeeftWedstrijdVolgendeMaandNietTerug(self):
        """Wedstrijddatum volgende maand wordt niet opgehaald"""
        self.fail("to be implemented")


    def testIndexGeeftWedstrijdVorigeMaandNietTerug(self):
        """Wedstrijddatum vorige maand wordt niet opgehaald"""
        self.fail("to be implemented")
