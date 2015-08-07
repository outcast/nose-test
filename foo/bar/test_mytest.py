__author__ = 'jajones3'


import foo

class TestMyClass():

    def setup(self):
        print "Setup class"

    def teardown(self):
        print "teardown class"

    def test_me(self):
        print "doing a test"