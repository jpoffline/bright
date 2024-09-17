import unittest
from .models import Member
from .matcher import matcher_params_from_member


class Test_matcher_params_from_member(unittest.TestCase):
    def test_all_false(self):
        member = Member(name="Member", bio="I'm a designer from London, UK")
        params = matcher_params_from_member(member)
        self.assertFalse(params.definite_location)
        self.assertFalse(params.negate_location)
        self.assertFalse(params.relocate_location)

    def test_negate_location(self):
        member = Member(
            name="Member", bio="I'm looking for a job in marketing outside of London"
        )
        params = matcher_params_from_member(member)
        self.assertFalse(params.definite_location)
        self.assertTrue(params.negate_location)
        self.assertFalse(params.relocate_location)

    def test_relocate(self):
        member = Member(
            name="Member",
            bio="I'm a software developer currently in Edinburgh but looking to relocate to London",
        )
        params = matcher_params_from_member(member)
        self.assertFalse(params.definite_location)
        self.assertFalse(params.negate_location)
        self.assertTrue(params.relocate_location)
