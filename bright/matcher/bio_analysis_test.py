import unittest
from ..models import Member
from . import matcher


def new_test_member(name: str, bio: str) -> Member:
    return Member(name=name, bio=bio)


class Test_bio_analysis_from_member(unittest.TestCase):
    def test_all_false(self):
        member = new_test_member(name="Member", bio="I'm a designer from London, UK")
        params = matcher.analyse_bio(member)
        self.assertFalse(params.definite_location)
        self.assertFalse(params.negate_location)
        self.assertFalse(params.relocate_location)

    def test_negate_location(self):
        member = new_test_member(
            name="Member", bio="I'm looking for a job in marketing outside of London"
        )
        params = matcher.analyse_bio(member)
        self.assertFalse(params.definite_location)
        self.assertTrue(params.negate_location)
        self.assertFalse(params.relocate_location)

    def test_relocate(self):
        member = new_test_member(
            name="Member",
            bio="I'm a software developer currently in Edinburgh but looking to relocate to London",
        )
        params = matcher.analyse_bio(member)
        self.assertFalse(params.definite_location)
        self.assertFalse(params.negate_location)
        self.assertTrue(params.relocate_location)
