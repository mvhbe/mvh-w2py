# -*- coding: utf-8 -*-

import unittest
import glob
import sys
import mvhutils
suite = unittest.TestSuite()

print "sys.argv : ", sys.argv

# get all files with tests
test_files = glob.glob('applications/' + sys.argv[2] + '/tests/*/*.py')

if not len(test_files):
    raise Exception("No files found for app: " + sys.argv[2])

# Bring all unit tests in and their controllers/models/whatever
for test_file in test_files:
    execfile(test_file, globals())

    # Create the appropriate class name based on filename and path
    # TODO: use regex
    filename =  str.capitalize(test_file.split("/")[-1][:-3])
    directory =  str.capitalize(test_file.split("/")[-2][:-1])

    suite.addTest(unittest.makeSuite(globals()[filename+directory]))

    # Load the to-be-tested file
    execfile("applications/"+ sys.argv[2] + "/" + directory.lower() +
             "s/" + filename.lower() + ".py", globals())


db = mvhutils.setupTestDb() # Use the test database for all tests

unittest.TextTestRunner(verbosity=2).run(suite)