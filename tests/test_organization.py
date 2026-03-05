import unittest
from src.org.organization import ClawTeam

class TestClawTeam(unittest.TestCase):

    def test_init(self):
        org = ClawTeam()
        self.assertIsNotNone(org.config)
