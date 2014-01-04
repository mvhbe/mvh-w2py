import unittest
from gluon.globals import Request, Session, Storage, Response
from testhelper import form_postvars

db = setupTestDb() # Use the test database for all tests
loggedIn = False


def login():
    insert_user()
    auth.user = db(db.auth_user.id > 0).select()
    loggedIn = True


def insert_user():
    db.auth_user.insert(first_name="first", last_name="last",
            email="first.last@telenet.be")

class KalenderController(unittest.TestCase):

    def setUp(self):
        if not loggedIn:
            login()
        request = Request({})


    def tearDown(self):
        db.kalender.truncate()
        db.wedstrijd.truncate()
        db.reeks.truncate()
        db.commit()


    def testOverzichtGeeftGeenKalendersTerugBijLegeDb(self):
        """Geen kalenders bij lege database"""
        response = overzicht()
        self.assertEqual(0, len(response["kalenders"]))
