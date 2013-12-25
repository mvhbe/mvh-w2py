import datetime
import unittest
from dateutil import relativedelta
from gluon.globals import Request, Session, Storage, Response

db = setupTestDb() # Use the test database for all tests

VANDAAG = datetime.datetime.now().date()
EEN_MAAND_GELEDEN = VANDAAG - relativedelta.relativedelta(months=-1)
EEN_MAAND_VERDER = VANDAAG + relativedelta.relativedelta(months=+1)

def insertWedstrijd(kalender=1,datum=VANDAAG,
                    omschrijving="Leden wedstrijd " +
                                 VANDAAG.strftime("%d/%m/%Y")):
    db.wedstrijd.insert(kalender=kalender, datum=datum,
                            omschrijving=omschrijving)

def insertReeks(wedstrijd=1,reeksnummer=1):
    db.reeks.insert(wedstrijd=wedstrijd, reeksnummer=reeksnummer)


def nieuweWedstrijd(datum=VANDAAG):
    insertWedstrijd(datum=datum)
    insertReeks()
    db.commit()


class DefaultController(unittest.TestCase):

    def setUp(self):
        request = Request({})


    def tearDown(self):
        db.wedstrijd.truncate()
        db.reeks.truncate()
        db.commit()


    def testIndexGeeftGeenWedstrijdenTerugBijLegeDb(self):
        """Geen wedstrijden bij lege database"""
        response = index()
        self.assertEqual(0, len(response["wedstrijden"]))


    def testIndexGeeftWedstrijdHuidigeMaandTerug(self):
        """Wedstrijddatum huidige maand wordt opgehaald"""
        nieuweWedstrijd()
        response = index()
        self.assertEqual(1, len(response["wedstrijden"]))


    def testIndexGeeftWedstrijdVolgendeMaandNietTerug(self):
        """Wedstrijddatum volgende maand wordt niet opgehaald"""
        nieuweWedstrijd(EEN_MAAND_VERDER)
        response = index()
        self.assertEqual(0, len(response["wedstrijden"]))


    def testIndexGeeftWedstrijdVorigeMaandNietTerug(self):
        """Wedstrijddatum vorige maand wordt niet opgehaald"""
        nieuweWedstrijd(EEN_MAAND_GELEDEN)
        response = index()
        self.assertEqual(0, len(response["wedstrijden"]))
