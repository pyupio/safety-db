import unittest
import json
from packaging.specifiers import SpecifierSet, InvalidSpecifier


class TestData(unittest.TestCase):

    def setUp(self):
        with open("data/insecure.json") as f:
            try:
                self.db = json.loads(f.read())
            except ValueError as e:
                self.fail("No valid json in insecure.json: {}".format(e),)

        with open("data/insecure_full.json") as f:
            try:
                self.db_full = json.loads(f.read())
            except ValueError as e:
                self.fail("No valid json in insecure_full.json: {}".format(e),)

    def test_data_in_sync(self):
        # test all packages are in sync
        for key in self.db.keys():
            self.assertTrue(key in self.db_full.keys())

        # test all pkg versions in the small db are also in the full db
        for pkg in self.db:
            db_versions = set(sorted(self.db[pkg]))
            db_full_versions = set(sorted(item["v"] for item in self.db_full[pkg]))
            self.assertEquals(
                db_versions,
                db_full_versions,
                "Versions for {} not matching\n{}\n{}".format(pkg, db_versions, db_full_versions)
            )

    def test_using_valid_specifier_sets(self):

        def test_spec(spec, db):
            try:
                SpecifierSet(spec)
            except InvalidSpecifier as e:
                self.fail("Invalid specifier in {db}: {e}".format(db=db, e=e))

        for specifiers in self.db.values():
            for specifier in specifiers:
                test_spec(specifier, "insecure.json")

        for values in self.db_full.values():
            for item in values:
                test_spec(item["v"], "insecure.json")


if __name__ == '__main__':
    unittest.main()
