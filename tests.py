import unittest
import json
from packaging.specifiers import SpecifierSet, InvalidSpecifier

from safety_db import INSECURE, INSECURE_FULL


class TestData(unittest.TestCase):

    def setUp(self):
        with open("data/insecure.json") as f:
            try:
                self.db = json.loads(f.read())
            except ValueError as e:
                self.fail("No valid json in insecure.json: {}".format(e),)

    def test_using_valid_specifier_sets(self):

        def test_spec(spec, db):
            try:
                SpecifierSet(spec)
            except InvalidSpecifier as e:
                self.fail("Invalid specifier in {db}: {e}".format(db=db, e=e))

        for specifiers in self.db.values():
            for specifier in specifiers:
                test_spec(specifier, "insecure.json")

    def test_main_module(self):
        self.assertTrue(len(INSECURE) > 0)
        self.assertTrue(len(INSECURE_FULL) > 0)


if __name__ == '__main__':
    unittest.main()
