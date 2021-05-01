import json
import unittest

from packaging.specifiers import InvalidSpecifier, SpecifierSet
from parameterized import parameterized

from safety_db import INSECURE, INSECURE_FULL


def generatePackageSpecifiers():
    with open("data/insecure.json") as f:
        database = json.loads(f.read())
    for pkg, all_specs in database.items():
        for spec in all_specs:
            if pkg == '$meta':
                continue
            else:
                yield pkg, spec


class TestData(unittest.TestCase):

    @parameterized.expand(generatePackageSpecifiers)
    def test_using_valid_specifier_sets(self, pkg, spec):
        message = f"Bad specifier for {pkg}: {spec!r}"
        try:
            specifier_set = SpecifierSet(spec)
        except InvalidSpecifier:
            specifier_set = None
        self.failUnless(specifier_set, msg=message)
        self.assertIsInstance(specifier_set, SpecifierSet, message)

    def test_main_module(self):
        self.assertTrue(len(INSECURE) > 0)
        self.assertTrue(len(INSECURE_FULL) > 0)


if __name__ == '__main__':
    unittest.main()
